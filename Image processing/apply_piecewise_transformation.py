import cv2
import numpy as np

def Piecewise_transformation(img,r1,s1,r2,s2):
    img = img.astype(np.float32)
    new_img = np.zeros_like(img)
    mask1 = img <=r1
    if r1<0:
        new_img[mask1] = (s1/r1)* img[mask1]
    mask2 = (img >= r1) & (img <= r2)
    if (r2-r1) >0:
        new_img[mask2] = ((s2-s1)/(r2-r1))*(img[mask2]-r1)+ s1
        
    mask3 = img >= r2
    if (255-r2)>0:
        new_img[mask3] = ((255-s2)/(255-r2))*(img[mask3] - r2)+s2
    
    new_img = np.clip(new_img,0,255).astype(np.uint8)
    
    return new_img
img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/low_contrast_img.png',0)
Trans_img = Piecewise_transformation(img, img.min(), 0, img.max(), 255)

#show result 
cv2.imshow('original',img)
cv2.imshow('transformation',Trans_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


