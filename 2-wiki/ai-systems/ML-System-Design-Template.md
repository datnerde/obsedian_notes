---
title: ML System Design — Interview Template
tags: [ai-systems, system-design, interview, mlops]
created: 2026-04-19
status: growing
related: [[AB Testing]], [[Feature Engineering]], [[Ensemble-Methods]]
source: Notion System Design
---

# ML System Design — Interview Template

> 6-step framework for ML system design interviews. Steps 4 (Data) and 5 (Model) are the core — spend ~60% of interview time here.

---

## Timing Guide

| Step | Time |
|---|---|
| 1. Clarify | 2–3 min |
| 2. Metrics | 2 min |
| 3. Architecture | 1–2 min |
| 4. Data ⭐ | 10–15 min |
| 5. Model ⭐ | 10–15 min |
| 6. Serving | 5 min |
| MLOps (woven through 4/5/6) | ask interviewer |

---

## Step 1 — Clarifying Requirements

Restate the problem in your own words. Then ask:

| Question | Why It Matters |
|---|---|
| How much data? | Small → simple model; large → deep learning viable |
| Hardware/time constraints? | Determines complexity budget |
| Latency vs. accuracy trade-off? | Shows you think in trade-offs |
| Need for retraining? | Affects pipeline and MLOps scope |

---

## Step 2 — Metrics

Always give at least **one offline + one online** metric.

- **Offline**: AUC, F1, Precision/Recall (classification); R², RMSE (regression); NDCG, MRR (ranking)
- **Online** (business-tied): CTR, watch time, CVR, revenue per impression — depends heavily on the problem
- **Non-functional** (show breadth): training speed, scalability, debuggability

---

## Step 3 — Architecture

High-level pipeline sketch: Data → Feature Store → Training → Evaluation → Serving → Monitoring.

---

## Step 4 — Data ⭐

### 4.1 Target Variable
- **Explicit labels**: direct observations (purchase = 1, no purchase = 0)
- **Implicit signals**: dwell time, scroll depth, saves — discuss pros/cons of each

### 4.2 Feature Design
- User features: demographics, historical behavior
- Item features: content attributes, freshness
- Context features: time, device, session

### 4.3 Feature Engineering
- Train/test split (avoid leakage — split on time for temporal data)
- Missing values: drop if data is abundant; impute with mean/median if scarce
- Class imbalance: up-sampling, down-sampling, SMOTE, class-weighted loss
- Normalization: required for linear models and distance-based models; not needed for trees

### 4.4 Feature Selection
- Deep learning: let the network learn representations (sparse → embedding)
- Traditional ML: tree-based feature importance; L1 regularization for automatic selection

### 4.5 Additional Considerations
- **Bias**: does training data represent the full population?
- **Privacy**: anonymization, PII removal, regulatory requirements

**MLOps — Data Layer:** S3/GCS for storage; Kafka/Flume for streaming ingestion; Spark/TF Transform for feature transformation; Airflow for orchestration; FEAST/SageMaker for feature store.

---

## Step 5 — Model ⭐

Follow **simple → complex** progression — always justify the progression:

### Baseline (no ML)
Start here. Example: recommend most popular items. Fast to ship, establishes the floor.

### Traditional ML
Logistic Regression, Decision Tree, Random Forest, XGBoost. Fast training, interpretable, strong on tabular data.

### Deep Learning
DNN, Two-Tower, Transformer. More expressive, better for unstructured data (text, image), needs more data and compute.

**For each model, cover:**
- Model description + key hyperparameters + loss function
- ✅ Advantages
- ❌ Disadvantages

**MLOps — Modeling:** MLflow/KubeFlow for experiment tracking; DVC/SageMaker for model versioning; cloud-native hyperparameter tuning.

---

## Step 6 — Serving & Monitoring

| Topic | Key Point |
|---|---|
| A/B Testing | Use online metrics defined in Step 2 |
| Inference location | Edge (low latency, high cost) vs. server (easy to update) |
| Monitoring | Error rate, query latency, metric scores, data drift |
| Bias & misuse | Does the model amplify demographic biases? |
| Retraining | Daily/weekly/monthly? Triggered by drift or on schedule? |

**MLOps — Serving:** ElasticSearch/Logstash for logging; Kibana/Splunk for analysis; CircleCI for CI/CD; quantization + distillation for edge deployment.

---

## Common Problem Types

| Problem | Key Design Decision |
|---|---|
| Recommendation | Two-Tower recall → ranking rerank; implicit vs explicit labels |
| Ad CTR prediction | Feature crosses; calibration; exploration vs exploitation |
| NLP classification | Pre-trained LLM fine-tuning vs. lightweight BoW for latency |
| Anomaly detection | Unsupervised (Isolation Forest, Autoencoder) vs. supervised with labels |
| Forecasting | Time-series split; lag features; trend + seasonality decomposition |

---

## Related

- [[AB Testing]] — online evaluation methodology
- [[Feature Engineering]] — feature pipeline detail
- [[Ensemble-Methods]] — model choice in Step 5
