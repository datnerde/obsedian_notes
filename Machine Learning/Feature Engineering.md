# 1.Normalization

- Reason:
    - Remove the impact on range & scale when comparing features for analysis
    - Gradient decent can find the optimal solution faster
- Methods:
    - Min-Max Scaling: linear transformation to range of [0,1]
    - 
        ![[Pictures/Untitled.png]]
    - Z-Score Normalization: transformation to N(0,1) distribution
    - ![[Pictures/Untitled 1.png]]
- Exceptions:
    - Decision tree related model will not be affected by normalization

# 2.Categorical Feature

- Method:
    - Ordinal Encoding
    - One-hot Encoding
        - Use sparse matrix to represent features
        - Can be used with feature selections to reduce dimensions
    - Binary Encoding
        - Hash map of ID to generate a representation of features that occupy less space compared to one-hot encoding

# 3.High Dimensional Space

- Feature Crosses(Feature Combinations)
    - We can use a dimension-reduced version to represent the feature spaces if we have too many dimensions from feature crosses

# 4.Feature Combinations

- Use decision-tree to look up combinations and represent them using sparse matrix

# 5.Text Representation Model

- Bag of Words & N-gram & Word Stemming
    - Considering document as a bag of words(1,2,or n as one group of word) without orders
    - Word stemming gets us the most basic form of the term
- TF-IDF(Term Frequency-Inverse Document Frequency)
    - TF-IDF(t,d) = TF(t,d) x IDF(t)
    - IDF(t) = log(num. of docs / num. of docs with term t + 1)
        - If a word is frequently appearing across docs, it is not an important word. We penalize it via IDF
- Topic Model
    - 
- Word Embedding (Deep Learning)
    - Sets of models to represent documents and words in a lower dimensional space
    - Words with similar meanings will tend to be represented similarly in lower space

# 6.Word2Vec(word embedding model)

- CBOW(Continues Bag of Words)
    - Predict probability of current word based on pre and after words
- Skip-gram
    - Predict pre and after words based on current word
![[Untitled 2 1.png]]
- LDA can be considered as a decomposition: doc x word = doc x topic * topic x word
- Word2Vec can be considered as learning about the words around the term x current term

# 7.Not Enough Graphical Data

- Model simplification
    - L1/ L2 regularization
    - Dropout
    - …
- Data Augmentation

#feature_engineering 