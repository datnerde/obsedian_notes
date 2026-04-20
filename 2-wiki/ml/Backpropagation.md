---
title: Backpropagation
tags: [ml, deep-learning, neural-networks, optimization]
created: 2026-04-19
status: growing
related: [[Optimization]], [[Overfitting and Underfitting]], [[KL-Divergence]]
source: Notion ML Proof
---

# Backpropagation

> **Core idea:** Efficiently compute gradients in a neural network by applying the chain rule backward through the computation graph. Time complexity = same order as forward pass.

---

## Setup (L-layer MLP)

For layer $l$:
- **Linear:** $z_l = W_l a_{l-1} + b_l$
- **Activation:** $a_l = \phi(z_l)$
- Input: $a_0 = x$, Output: $a_L = \hat{y}$, Loss: $\mathcal{L}(\hat{y}, y)$

---

## Forward Pass

Compute $z_l$ and $a_l$ layer-by-layer from $l=1$ to $L$. **Save all intermediate values** — backward pass needs them.

---

## Backward Pass

**Step 1: Define the error term**

$$\delta_l \triangleq \frac{\partial \mathcal{L}}{\partial z_l}$$

This is the gradient of loss w.r.t. the *pre-activation* output at layer $l$.

**Step 2: Output layer base case**

$$\delta_L = \frac{\partial \mathcal{L}}{\partial a_L} \odot \phi'(z_L)$$

For cross-entropy + softmax: $\delta_L = p - y$ (remarkably clean — predicted minus true).

**Step 3: Hidden layer recursion (key formula)**

$$\boxed{\delta_l = (W_{l+1}^T \delta_{l+1}) \odot \phi'(z_l)}$$

Intuition: error at layer $l$ = error from layer $l+1$ routed back through weights, scaled by activation derivative.

**Step 4: Weight and bias gradients**

$$\boxed{\frac{\partial \mathcal{L}}{\partial W_l} = \delta_l \cdot a_{l-1}^T}$$

$$\frac{\partial \mathcal{L}}{\partial b_l} = \delta_l$$

---

## Why Backprop is Efficient

Naive approach (finite differences): $O(P)$ forward passes for $P$ parameters.

Backprop: one forward + one backward = $O(1)$ passes regardless of $P$. Each layer computed once in each direction.

---

## Vanishing / Exploding Gradients

The recursion $\delta_l = W_{l+1}^T \delta_{l+1} \odot \phi'(z_l)$ involves a product of $L-l$ Jacobians:

$$\frac{\partial \mathcal{L}}{\partial z_1} = \prod_{l=1}^{L} \frac{\partial z_{l+1}}{\partial z_l} \cdot \frac{\partial \mathcal{L}}{\partial z_L}$$

- If eigenvalues of Jacobian $< 1$ consistently: **vanishing gradient** — deep layers learn very slowly (sigmoid, tanh)
- If eigenvalues $> 1$ consistently: **exploding gradient** — training diverges

**Solutions:**
- ReLU activation ($\phi'(z) = 1$ for $z > 0$) — avoids saturation
- Residual connections — gradient highway bypassing layers
- Gradient clipping — for exploding gradients
- BatchNorm — stabilizes layer input distributions → smooths loss landscape

---

## Connection to Optimization

Backprop computes gradients; [[Optimization]] (SGD, Adam, RMSProp) uses them to update weights.

- SGD: $W_l \leftarrow W_l - \eta \nabla_{W_l} \mathcal{L}$
- Adam: adaptive per-parameter learning rates using first and second gradient moments
