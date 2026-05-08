import cv2
import numpy as np

img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/Noisy_img.jpg',0)

kernel = np.ones((3,3),np.uint8)
_,img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# morphological erosion 
erosion = cv2.erode(img,kernel,iterations = 1)

# morphological dilation
dilation= cv2.dilate(img,kernel,iterations = 1)

# compound operation - Open 
# first erosion then dilation
#open_img = cv2.dilate(erosion,kernel,iterations = 1)

open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


# compound operation -  Close
# first dilation then erosion

#close_img = cv2.erode(dilation,kernel,iterations = 1)

close_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# showing result
cv2.imshow('original', img)
cv2.imshow('Erosion',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()