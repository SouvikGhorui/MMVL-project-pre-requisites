# Computer Vision & Machine Learning: 3rd Semester Project

This repository is a structured learning path and codebase for my 3rd-semester project on **Computer Vision**. It tracks my progress through fundamental **Image Processing**, **Classical Machine Learning**, and upcoming **Deep Learning** topics.

---

## 📚 Project Syllabus & Progress Tracker

### 1. Image Processing and Computer Vision
Focused on spatial domain manipulation and mathematical foundations.

- [x] **2.1 - 2.2 Read & Write Images** (`16-understanding_digital_images.py`, `17-Reading_images_in_python.py`, `Pillow_library.py`)
- [x] **2.3 Color to Grayscale/BW** (Implemented across various scripts)
- [x] **2.4 Horizontal & Vertical Reverse** (`horizontalVartical.py`)
- [x] **2.5 Image Cropping** (`crop.py`)
- [x] **2.6 Image Negative** (`inverseImg.py`)
- [x] **2.7 Filters (Mean, Gaussian, Median)** (`Extras/Karnels_in_Gaussian_blur.py`)
- [x] **2.8 - 2.11 Edge & Gradient Detection** (`Edge_detection.py`, `Otsu's Algorithm`)
- [x] **2.12 Image Difference** (`Finding_difference_of_two_images.py`)
- [x] **2.13 Rotation** (`rotate_image_in_different_orientions.py`)
- [x] **2.14 - 2.32 Vectorization & Major Ordering** (`Row_major_and_column_major.py`)
- [x] **2.15 & 2.21 Segmentation (Grabcut/Background)** (`Foreground_and_Background_segmentation.py`, `Image_segmentation_Grabcut.py`)
- [x] **2.16 - 2.17b Histogram Operations** (`Histogram_of_an_image.py`, `Histogram_Equalizer_and_CLAHE.py`, `Histogram_matching.py`, `Histogram_normalization.py`)
- [x] **2.18 - 2.18b Noise & Thresholding** (`Add_and_remove_noise.py`, `Threshold_using_histogram.py`)
- [x] **2.19 Linear, Piece-wise & Gamma Correction** (`apply_linear_transformation.py`, `apply_piecewise_transformation.py`, `Apply_gamma-correction.py`)
- [x] **2.20 Morphological Operations** (`Morphological_operations.py`)
- [x] **2.22 - 2.24 Interpolation (Spline, Linear, Bilinear)** (`spline_interpolation.py`, `Bilinear_interpolation.py`)
- [x] **2.27 - 2.31 Distance Metrics** (`cosine_sine_distances.py`, `Euclidian_spaces.py`, `Geodesic_distance.py`, `Manhattan_distance.py`, `Minkowski_distance.py`)
- [x] **2.34 Otsu's Algorithm** (`Otsu's Algorithm (Histogram Thresholding).py`)

### 2. Machine Learning
Implementation of classical ML algorithms from scratch and using libraries.

- [x] **3.1 KNN Classifier** (`KNN_scratch.ipynb`)
- [ ] **3.2 Minimum Distance Classifier**
- [x] **3.3 - 3.5 Regression (Linear, Multiple, Logistic)** (`linear_regression.ipynb`, `MultipleLinearRegression.ipynb`, `Logistic_regression.ipynb`)
- [ ] **3.6 SVM**
- [x] **3.7 Random Forest & Decision Tree** (`RandomForest.ipynb`, `decision_tree.ipynb`)
- [x] **3.8 Bag of Words** (`BagofWords.ipynb`)
- [x] **3.10 PCA** (`PCA.ipynb`, `Dimensionality Reduction & Feature Extraction.ipynb`)
- [x] **3.11 - 3.14 Clustering (K-means, K-medoid, Hierarchical, DBScan)** (Various `.ipynb` files)
- [x] **3.15 HOG Feature Extraction** (`HOG.ipynb`)
- [x] **3.15 LBP (Local Binary Patterns)** (`LBP.ipynb`)
- [x] **Classification on MAGIC Gamma Telescope Data** (`MagicGemmaTelescope.ipynb`)
- [x] **Mini Project: MNIST** (Augmentation, PCA, HOG, Logistic Regression, Random Forest) (`MiniProject.ipynb`)

### 3. Deep Learning 🚀
Implementations using **TensorFlow** and **PyTorch**.

- [x] **4.0 TensorFlow Basics** (`Deep learning/tersorflow.ipynb`)
- [x] **4.1 ANN for Classification & Regression** (`Deep learning/tersorflow.ipynb`)
- [x] **4.2 PyTorch Basics** (`Deep learning/PytorchBasics.ipynb`)
- [ ] **4.3 Neural Networks**
    - [x] 4.3a Perceptron (`Deep learning/DataPipeline.ipynb`)
    - [x] 4.3b Multilayer Perceptron (`Deep learning/NN.ipynb`)
    - [x] 4.3c Back Propagation (Risk minimization, Gradient Descent, Calculus) (`Deep learning/Autograd.ipynb`)
    - [ ] 4.3d Universal Approximation
    - [ ] 4.3e Loss Functions (Different types & choosing a loss function)
    - [ ] 4.3f Training (Batch Size, SGD, Mini batch, second order methods)
    - [ ] 4.3g Optimization (Optimizers, Regularizers, Batch Normalization, Dropout)
- [ ] **4.4 Convolutional Neural Network (CNN)**
    - [ ] 4.4a Models of Vision and CNNs
    - [ ] 4.4b Training the CNNs
    - [ ] 4.4c Visualization (Layers of CNNs, GradCam, TSNE Plot)
    - [ ] 4.4d Transpose Convolution
- [ ] **4.5 Auto-Encoders** (Auto-Encoder, Convolutional Auto-Encoder, Denoising Auto-Encoder)
- [ ] **4.6 Sequence Models** (RNN, LSTM, GRU)
- [ ] **4.7 Image Classification Models** (ResNet, VGG, DenseNet, MobileNet)
- [ ] **4.8 Object Detection** (RCNN, Fast/Faster/Mask/Grid RCNN, SSD, YOLO)
- [ ] **4.9 Image Segmentation** (SegNet, UNet)
- [ ] **4.10 Generative Networks**
    - [ ] 4.10a VAE (Variational Auto-Encoder)
    - [ ] 4.10b GAN (Generative Adversarial Networks)
    - [ ] 4.10c DC GAN, Cycle GAN
    - [ ] 4.10d Diffusion Models
- [ ] **4.11 Foundational Models**
    - [ ] 4.11a Transformer, Attention Models
    - [ ] 4.11b Vision Transformers (ViT, Swin, DinoV2)
    - [ ] 4.11c Transformer Models for Segmentation & Detection (Trans UNET, Swin UNET)

---

## 🔗 Useful Resources

### Image Processing
*   [Digital Image Processing using Python (YouTube)](https://www.youtube.com/watch?v=zDWJUSeuiZs&list=PLx3nvcXDbLZPvTKFuyxQ-A847SWbQrsts)
*   [Image Processing using OpenCV (YouTube)](https://www.youtube.com/watch?v=oUJs03eZ0S8&list=PLKnIA16_RmvYXDBJ5WRDuQRSzFJs93pYR&index=1)
*   [Digital Image Processing Course](https://www.youtube.com/watch?v=52pMFnkDU-4&list=PLZsOBAyNTZwYx-7GylDo3LSYpSompzsqW&index=2)

### Machine Learning
*   [CMU Machine Learning Notes](https://www.cs.cmu.edu/~mgormley/courses/10601/)
*   [Stanford CS229: Machine Learning](https://cs229.stanford.edu/)
*   [Bag of Visual Words Explained](https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb)

### Deep Learning
*   [PyTorch Tutorials](https://pytorch.org/tutorials/)
*   [TensorFlow Documentation](https://www.tensorflow.org/learn)
*   [CMU Deep Learning Course](https://deeplearning.cs.cmu.edu/F24/index.html)
*   [Stanford CS231n: Deep Learning for Computer Vision](https://cs231n.stanford.edu/)
*   [Stanford CS230: Deep Learning](https://cs230.stanford.edu/syllabus/)

---

## 🛠️ Tech Stack
*   **Languages:** Python
*   **Libraries:** OpenCV, Pillow, Scikit-learn, NumPy, Pandas, Matplotlib, TensorFlow, PyTorch
*   **IDE:** VS Code, Jupyter Notebooks
