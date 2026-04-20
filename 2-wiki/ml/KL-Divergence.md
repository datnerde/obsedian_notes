---
title: KL Divergence
tags: [ml, statistics, information-theory, deep-learning]
created: 2026-04-19
status: growing
related: [[Overfitting and Underfitting]], [[Backpropagation]], [[Logistic Regression]]
source: Notion ML Proof
---

# KL Divergence

> **Core idea:** KL divergence measures how much information is lost when distribution $Q$ is used to approximate $P$. It is non-negative and asymmetric — it is *not* a true distance metric.

---

## Definition

$$D_{KL}(P \| Q) = E_P\left[\log \frac{P(x)}{Q(x)}\right] = \sum_x P(x) \log \frac{P(x)}{Q(x)}$$

(Replace $\sum$ with $\int$ for continuous distributions.)

**Intuition:** Using $Q$ to encode data drawn from $P$. The KL divergence is the extra bits per sample compared to using the true distribution $P$.

---

## Proof: $D_{KL} \geq 0$ (Gibbs' Inequality)

By Jensen's inequality (since $\log$ is concave):

$$D_{KL}(P \| Q) = -E_P\left[\log \frac{Q}{P}\right] \geq -\log E_P\left[\frac{Q}{P}\right] = -\log \sum_x Q(x) = 0$$

$$\boxed{D_{KL}(P \| Q) \geq 0 \text{, with equality iff } P = Q}$$

---

## Asymmetry

$D_{KL}(P \| Q) \neq D_{KL}(Q \| P)$ in general.

- $D_{KL}(P \| Q)$: penalizes regions where $P$ has mass but $Q$ does not → *mode-seeking* behavior
- $D_{KL}(Q \| P)$: penalizes regions where $Q$ has mass but $P$ does not → *mean-seeking* behavior

This matters in variational inference: minimizing $D_{KL}(Q \| P)$ (the "reverse KL") produces sharper approximate posteriors than the forward KL.

---

## Connection to Cross-Entropy

$$H(P, Q) = -\sum_x P(x) \log Q(x) = \underbrace{H(P)}_{\text{entropy}} + \underbrace{D_{KL}(P \| Q)}_{\text{KL divergence}}$$

Since $H(P)$ is constant w.r.t. model parameters:

$$\boxed{\text{minimizing cross-entropy loss} \equiv \text{minimizing KL divergence from model to data}}$$

This is why categorical cross-entropy is the natural loss for classification — it pushes the model distribution toward the true label distribution.

---

## Applications

| Context | Role of KL |
|---|---|
| **Classification (cross-entropy loss)** | Minimizing $H(P,Q)$ = minimizing $D_{KL}(P \| Q)$ |
| **Variational Autoencoder (VAE)** | ELBO = $E[\log p(x\|z)] - D_{KL}(q(z\|x) \| p(z))$ — KL term regularizes latent space |
| **Knowledge Distillation** | Student minimizes KL to teacher's softmax output |
| **RL (PPO)** | KL constraint prevents policy from deviating too far from old policy |

---

## Related

- [[Logistic Regression]] — cross-entropy loss derived from MLE = minimizing KL
- [[Backpropagation]] — gradient of cross-entropy loss via chain rule
