import cv2
import numpy as np

img1 = cv2.imread('Photos/p-100x100.jpg',0)
img2 = cv2.imread('Photos/r-185x200.jpg',0)

# we want the images have same dimensions, if not, the operations are not possible 
img2=cv2.resize(img2,img1.shape)
print(img2.shape)

dist = np.linalg.norm(img1.astype(float)-img2.astype(float))
print(dist)
