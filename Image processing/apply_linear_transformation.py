import cv2
import matplotlib.pyplot as plt

def ApplyLinearTrans(img, alpha, beta):
    # G(x) = alpha * f(x) + beta
    #alpha: Contrast control (1.0-3.0)
    #beta: Brightness control (0-100)
    Transformed_img = cv2.convertScaleAbs(img,None,alpha = alpha, beta = beta)
    return Transformed_img

img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/test_flower.jpg',0)
img_trasformed = ApplyLinearTrans(img, 1.1, 40)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv2.cvtColor(img_trasformed, cv2.COLOR_BGR2RGB))
plt.show()