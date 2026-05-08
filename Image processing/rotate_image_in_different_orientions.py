import cv2

img = cv2.imread(r"Photos/photo_1.webp")

cv2.imshow("Original",img)
height, weight,_ =img.shape
T = cv2.getRotationMatrix2D((weight/2,height/2),45,1)
img_trans = cv2.warpAffine(img, T, (height, weight))

cv2.imshow("Rotation",img_trans)

cv2.waitKey(0)
cv2.destroyAllWindows()
