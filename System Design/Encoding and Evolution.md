# Chapter 4: Encoding and Evolution

- Backward compatibility means newer code can read data written by older code. Forward compatibility means older code can read data written by newer code.
- Forward compatibility is trickier because it requires older code to ignore additions made by a newer version of the code.

## Formats for Encoding Data

### Language-Specific Formats

- Using a language's built-in encoding functionality is bad from interoperability, security, efficiency, and versioning perspectives.
- JSON, XML, and Binary Variants
    - JSON distinguishes strings and numbers, but it doesn't distinguish integers and floating-point numbers, and it doesn't specify a precision.
    - Base64-encoding a binary string to use it in XML or JSON increases the data size by 33%.
    - Simply having different organizations agree on a single format is far more important than the aesthetics or efficiency of a format.
- Binary encoding
    - Because JSON and XML don't prescribe a schema, they need to include all the object field names within the encoded data.
    - It's not clear whether the small space reduction by MessagePack, a binary encoding for JSON, is worth the loss of human-readability.
        - **Thrift and Protocol Buffers**
            - Confusingly, Thrift has two binary encoding formats, called _BinaryProtocol_ and _CompactProtocol_.
            - Field tags are like aliases for fields – they are a compact way of saying what field we're talking about without spelling out its name.
            - Variable length integers use the top bit of each byte to specify whether there are still more bytes to come.
            - With variable length integers, the numbers -64 to 63 are encoded in one byte, -8192 to 8191 are encoded in two bytes, etc. Bigger numbers use more bytes.
            - The `required` keyword of Protocol Buffers enables a runtime check that fails if the field is not set, which is useful for catching bugs.
        - **Field tags and schema evolution**
            - With Thrift and Protocol Buffers, you can change a field name, but changing its tag renders all existing encoded data invalid.
            - If old code reads data written by new code, including a new field with an unrecognized tag, it can simply ignore that field. This maintains forward compatibility.
        - **Datatypes and schema evolution**
            - With Protocol Buffers, it's okay to change an `optional` (single-valued) field into a `repeated` (multi-valued) field.
        - **Avro**
            - Avro has two schema languages: Avro IDL is intended for human editing, and a JSON equivalent that is more easily machine-readable.
            - An encoded byte string specifies nothing to identify fields or their data types. It simply consists of values concatenated together.
            - Consequently the binary data can only be decoded correctly if the code reading the data is using the _exact same schema_ as the code that wrote the data.
        - The writer's schema and the reader's schema
            - While decoding data, Avro resolves the differences between the _writer's schema_ and the _reader's schema_, and translates read data from the former to the latter. This enables schema evolution.
        - Schema evolution rules
            - Adding a field that has no default value breaks backward compatibility. Removing a field that has no default value breaks forward compatibility.
            - Avro doesn't have `optional` or `required` keywords like Thrift and Protocol buffers, but instead allows defining union types with `null` as a value.
        - Dynamically generated schemas
            - Because an Avro schema doesn't define tag numbers, it is friendlier to dynamically generated schemas, e.g. creating an Avro schema from a relational database schema.

### The Merits of Schemas

- Database vendors provide a driver (e.g. using the ODBC or JDBC APIs) that decode responses from a database's network protocol into in-memory data structures.
- Schema evolution allows the same flexibility as schemaless/schema-on-read JSON databases, while also providing better guarantees about your data and better tooling.

## Modes of Dataflow

### Dataflow through Databases

- In an environment where the application is changing, it's likely that some processes accessing the database will be running newer code and some will be running older code.
- Consequently a value in the database might be written by a newer version of the code, and then later read by an older version. And so forward compatibility is required.
- If an application decodes a database value into model objects, and then later re-encodes those model objects, the unknown fields may be lost in that translation process.
    - Different values written at different times
        - Data outlives code: While deploys may replace older code with newer code within minutes, data in the database may have last been encoded and written years ago.
        - Rewriting (migrating) data into a new schema is possible, but it is expensive on a large data set, and so most databases avoid it if possible.
        - Schema evolution allows a database to appear as if it was encoded with a single schema, although the underlying storage may contain records encoded with various historical schema versions.

### Dataflow Through Services: REST and RPC

- The application-specific APIs of services provide encapsulation, by restricting what clients can and cannot do.
- A key design goal of service-oriented/microservices architecture is to make the application easier to change and maintain by making services independently deployable and evolvable.
- Web services
    - The two popular approaches to web services are REST and SOAP.
    - REST emphasizes data formats, using URLs for identifying resources and using HTTP features for cache-control, authentication, and content-type negotiation.
    - SOAP is an XML protocol for API requests, and comes with a sprawling set of related standards (the _web standards framework_, or _WS-_) that add various features.
    - The API of a SOAP web service is described using an XML-based language called the Web Services Descriptive Language, or WSDL. WSDL enables code generation so that a client can access a remote service using local classes and method calls.
    - WSDL is not designed to be human-readable, and SOAP messages are often too complex to construct manually, so tooling, code generation, and IDEs fill in the gaps.
    - Despite the ostensible standards, interoperability between different vendors' implementations often causes problems in practice.
- The problems with remote procedure calls (RPCs)
    - The RPC model tries to make a request to a remote service look the same as calling a method within the same process – an abstraction called _location transparency_.
    - Variable latency, timeouts, retries and idempotence semantics, and serialization all mean there's no point in location transparency. Calling a remote service is fundamentally different.
- Current directions for RPC
    - The new generation of RPC frameworks is more explicit about the fact that a remote request is different from a local function call.
    - RESTful APIs have the advantage of being good for experimentation and debugging, support by all mainstream programming languages and platforms, and a vast ecosystem of available tools.
    - For these reasons, REST is used for public APIs, while RPC frameworks mostly focus on requests between services owned by the same organization.
- Data encoding and evolution for RPC
    - Between services using RPC, we assume servers will be updated first, and clients second. You therefore need backward compatibility on requests, and forward compatibility on responses.
    - The backward and forward compatibility properties of an RPC scheme are inherited from whatever encoding it uses, such as Thrift or gRPC.

### Message-Passing Dataflow

- In _asynchronous message-passing_ systems, messages are delivered to an intermediary called a _message broker_ which stores the message temporarily.
- Message brokers can act as a buffer if the recipient is unavailable or overloaded, redeliver messages to crashed processes, deliver messages to multiple recipients, and decouple producers and consumers.
- Message brokers
    - A process sends a message to a named _queue_ or _topic_, and the broker ensures delivery of the message to one or more _consumers_ or _subscribers_ of that queue or topic.
- Distributed actor frameworks
    - In the _actor model_, logic is encapsulated by actors that communicate via asynchronous messages, where delivery of each message is not guaranteed (even within the same process).
    - In a _distributed actor framework_, location transparency works better than with RPC, because the actor model already assumes that messages may be lost.
    - A distributed actor framework essentially integrates a message broker and the actor programming model into a single framework.