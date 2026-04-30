---
tags:
  - ai
  - python
  - course
  - learning
---

# Projects 5: Neural Networks

**CS50's Introduction to Artificial Intelligence with Python**

---

## Project — Traffic

**Build a CNN to classify road signs using the German Traffic Sign Recognition Benchmark (GTSRB).**

### Background

Autonomous vehicles need to identify road signs from camera images. The GTSRB dataset contains thousands of images of **43 different road sign categories**.

This project uses TensorFlow to design, train, and evaluate a convolutional neural network for this classification task.

### Getting Started

```bash
pip3 install -r requirements.txt  # opencv-python, scikit-learn, tensorflow
```

**Dataset structure:**
```
gtsrb/
  0/   ← 43 subdirectories, one per sign category
  1/
  ...
  42/
```

Place the `gtsrb` folder inside the project directory.

### Code Structure

`traffic.py` — `main()` orchestrates the workflow (pre-built):
1. Load data via `load_data`
2. Split into training and test sets
3. Get compiled model via `get_model`
4. Train, evaluate, optionally save

### Specification

Implement 2 functions:

**`load_data(data_dir)`**

Returns `(images, labels)` tuple:
- Read images using OpenCV (`cv2`)
- Resize all images to `IMG_WIDTH × IMG_HEIGHT` (constants defined in file)
- Images as numpy arrays, labels as integers (0–42)
- Use `os.path.join` for platform-independent paths

```python
import cv2
img = cv2.imread(filepath)
img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
```

**`get_model()`**

Returns a compiled TensorFlow/Keras model:
- Input shape: `(IMG_WIDTH, IMG_HEIGHT, 3)` (RGB images)
- Output layer: `NUM_CATEGORIES` units (43), `softmax` activation
- Architecture is up to you — experiment with:
  - Number of conv/pooling layers
  - Filter counts and sizes
  - Hidden layer sizes
  - Dropout rates

```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu",
                           input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

### Documentation Requirement

Create a `README.md` documenting your experiments:
- What architectures did you try?
- What worked well and what didn't?
- Key observations

### Constraints

- Only modify `load_data` and `get_model`
- Authorized imports: TensorFlow, OpenCV, scikit-learn, NumPy, Pandas
- When submitting via Git, **exclude the gtsrb directory** (too large)

### Running

```bash
python traffic.py gtsrb
python traffic.py gtsrb model.h5  # to save the model
check50 ai50/projects/2024/x/traffic
style50 traffic.py
```
