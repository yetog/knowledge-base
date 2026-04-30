---
tags:
  - ai
  - python
  - course
  - learning
---

# Week 5: Neural Networks

**CS50's Introduction to Artificial Intelligence with Python**

---

## Biological Inspiration

Biological neurons connect to form networks that receive and transmit electrical signals. When input surpasses a threshold, the neuron fires and forwards its signal.

An **Artificial Neural Network** is a computational framework modeled on this biological system. Networks map inputs to outputs based on their structure and learned parameters — training data shapes the configuration.

Each biological neuron's equivalent in AI is a **unit** linked with other units.

**Basic hypothesis function:** `h(x₁, x₂) = w₀ + w₁x₁ + w₂x₂`
- w₁, w₂ = weights
- w₀ = bias

---

## Activation Functions

Translate hypothesis function outputs into decisions.

| Function | Behavior |
|---|---|
| **Step Function** | Output 0 before threshold, then 1 |
| **Logistic Function** | Output between 0 and 1 (graduated confidence) |
| **ReLU (Rectified Linear Unit)** | Any positive output; negatives become 0 |

---

## Network Structure

**Layers:**
- **Input units** — receive raw features
- **Hidden units** — intermediate processing
- **Output units** — produce final predictions

Each output unit: multiplies inputs by weights, adds bias, applies activation function *g*.

**OR function example:** With inputs x₁ and x₂, unit weights of 1, and bias of -1:
```
g(-1 + 1×x₁ + 1×x₂)
```
Produces correct outputs when thresholded at 0.

---

## Gradient Descent

Minimizes loss during training by adjusting weights.

1. Start with random weights
2. Compute gradients across all data points
3. Update weights in the direction that reduces loss

| Variant | Description |
|---|---|
| **Standard Gradient Descent** | Uses all data points |
| **Stochastic Gradient Descent** | Uses a single randomly-selected point |
| **Mini-Batch Gradient Descent** | Uses small random samples — balances cost and precision |

---

## Multilayer Networks

Networks with input, output, and one or more **hidden layers** enable modeling non-linear data.

- **Perceptrons** only create linear decision boundaries — fail for non-linearly separable data
- Multiple hidden layers overcome this limitation

---

## Backpropagation

Training algorithm for networks with hidden layers:

1. Calculate output layer errors
2. Propagate errors **backward** layer by layer
3. Update weights progressively

Networks with multiple hidden layers are called **deep neural networks**.

---

## Overfitting Prevention

**Dropout:** Randomly deactivates units during training, preventing over-reliance on individual units. All units function normally after training.

---

## TensorFlow Example

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(n_features,)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10)
```

**Dense layers** connect every node in one layer to all nodes in the previous layer.

---

## Computer Vision

Images are made of pixels represented by **RGB values (0–255 each)**. Direct neural networks on raw pixels face two problems:
1. Ignores spatial structure
2. Requires excessive weight calculations

### Image Convolution

Applies a **kernel matrix** across an image, weighting each pixel by neighboring values. Different kernels serve different purposes — edge detection kernels highlight boundaries by amplifying pixel differences.

### Pooling

**Max-Pooling** reduces input dimensions by sampling region-wise maximum values, leveraging similarity of adjacent pixels.

### Flattening

Converts processed images into format suitable for traditional neural network layers.

### Convolutional Neural Networks (CNNs)

Combine convolution, pooling, and dense layers for image analysis:

1. Extract features through learned convolution filters
2. Reduce dimensionality through pooling
3. Feed flattened results into dense layers

Convolution + pooling together reduce **sensitivity to image variations** — slightly different angles produce comparable outputs.

---

## Recurrent Neural Networks (RNNs)

Unlike **feed-forward networks** that produce fixed outputs, RNNs use their **own outputs as subsequent inputs**.

This enables variable-length outputs, making them suitable for:
- Image captioning
- Video analysis
- Machine translation
- Sequential data processing

The non-linear architecture processes sequences iteratively, generating outputs at multiple steps until completion.
