import cv2
import numpy as np

img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/test_flower.jpg')
img = cv2.resize(img, (500,500))

# define mask
mask = np.zeros((img.shape[:2])).astype(np.uint8)
# define the rectangle in which the foregrond in present
rect = (30,16,445,345)

bgdModel = np.zeros((1,65),np.float64)
fgdModel= np.zeros((1,65),np.float64)

# its changes the mask and add 0-3 values in mask
# 0: sure backgroud 1: sure foreground 2: probable background 3: foreground
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount= 5,mode = cv2.GC_INIT_WITH_RECT)


mask2 = np.where(((mask==2)|(mask==0)),0,1).astype(np.uint8)

img_segmented = img* mask2[:,:,np.newaxis]


# showing result
cv2.imshow('Original image',img)
cv2.imshow('Grabcut image',img_segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()