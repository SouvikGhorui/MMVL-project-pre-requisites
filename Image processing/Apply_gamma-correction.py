import cv2
import numpy as np

def gamma_correction(img,gamma):
    table = np.array([((i/255.0)**gamma)*255 for i in range(256)]).astype(np.uint8)
    return cv2.LUT(img,table)

    
img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/low_contrast_img.png',0)
corrected_img = gamma_correction(img, 2.20)

#showing result 
cv2.imshow('original',img)
cv2.imshow('Gamma correction',corrected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
