# Computer Vision & Machine Learning: 3rd Semester Project

This repository serves as a comprehensive learning resource and codebase for my 3rd-semester project on **Computer Vision**. It covers fundamental concepts in **Image Processing** and **Machine Learning**, bridging the gap between raw data manipulation and intelligent decision-making.

## 📌 Project Overview
The goal of this project is to master the core principles required for building advanced computer vision systems. The repository is organized into two primary domains:
1. **Image Processing:** Low-level and mid-level operations on digital images using Python.
2. **Machine Learning:** Classical algorithms and feature extraction techniques applied to various datasets.

---

## 📂 Directory Structure

### 🖼️ Image Processing
Located in the `/Image processing` folder, this section contains scripts implementing various spatial and frequency domain techniques.

*   **Foundations:** Understanding digital images, reading/writing with OpenCV and Pillow.
*   **Transformations:** Linear, Piecewise-Linear, and Gamma correction.
*   **Interpolation:** Bilinear and Spline interpolation for resizing.
*   **Histogram Analysis:**
    *   Histogram Calculation & Normalization.
    *   Histogram Equalization & CLAHE.
    *   Histogram Matching and Thresholding (including Otsu's Algorithm).
*   **Noise & Filtering:** Adding and removing noise, Gaussian blur kernels.
*   **Segmentation:**
    *   Foreground and Background segmentation.
    *   GrabCut algorithm.
    *   Edge Detection.
*   **Mathematical Foundations:** 
    *   Distance metrics: Euclidean, Manhattan, Minkowski, Cosine, Sine, and Geodesic distances.
    *   Morphological operations (Erosion, Dilation, etc.).
    *   Row-major vs. Column-major storage.

### 🤖 Machine Learning
Located in the `/Machine learning` folder, this section contains Jupyter Notebooks exploring supervised and unsupervised learning.

*   **Regression:** Linear Regression, Multiple Linear Regression, and Logistic Regression.
*   **Clustering (Unsupervised):**
    *   K-Means & K-Medoids.
    *   DBSCAN (Density-Based Spatial Clustering of Applications with Noise).
    *   Hierarchical Clustering.
*   **Classification:**
    *   K-Nearest Neighbors (KNN) from scratch.
    *   Decision Trees and Random Forests.
*   **Feature Extraction & Dimensionality Reduction:**
    *   **PCA (Principal Component Analysis):** Reducing feature space while retaining variance.
    *   **HOG (Histogram of Oriented Gradients):** Essential for object detection.
    *   **Bag of Words (BoW):** Feature representation for image/text classification.
*   **Case Studies:** Analysis of the Magic Gamma Telescope dataset.

---

## 🛠️ Tech Stack
*   **Languages:** Python
*   **Libraries:** 
    *   `OpenCV` (Computer Vision)
    *   `Pillow` (PIL Fork - Image manipulation)
    *   `Scikit-learn` (Machine Learning)
    *   `NumPy` & `Pandas` (Data Processing)
    *   `Matplotlib` (Visualization)
*   **Environment:** Jupyter Notebooks & Python Scripts

---

## 🚀 Future Roadmap
*   [ ] **Deep Learning Foundations:** Neural Networks from scratch.
*   [ ] **Convolutional Neural Networks (CNNs):** Implementing architectures like LeNet, AlexNet, and VGG.
*   [ ] **Object Detection:** Exploring YOLO (You Only Look Once) and SSD.
*   [ ] **Transfer Learning:** Utilizing pre-trained models for custom tasks.

---

## 📝 Usage
Each script in the `Image processing` folder is a standalone Python file. To run them:
```bash
python "Image processing/filename.py"
```
The machine learning modules are provided as `.ipynb` files and can be opened using Jupyter Lab, Jupyter Notebook, or VS Code's Interactive Window.
