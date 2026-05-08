import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Photos/low_contrast_img.png')

# applying min- max normalization and converting to RGB
normalized_img =cv2.normalize(img, None,alpha = 0,beta = 255, norm_type = cv2.NORM_MINMAX)
normalized_img = cv2.cvtColor(normalized_img, cv2.COLOR_BGR2RGB)

# appplying general equlization
# converting to RGB
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
(l,a,b) = cv2.split(lab_img)
equ = cv2.equalizeHist(l)
equ_img = cv2.merge((equ,a,b))
equ_img = cv2.cvtColor(equ_img, cv2.COLOR_LAB2RGB)

# drawing hsitograms
hist_img = cv2.calcHist([img],[0],None, [256], [0,256])
hist_equ_img = cv2.calcHist([equ_img],[0],None, [256], [0,256])
hist_normalized_img = cv2.calcHist([normalized_img],[0],None, [256], [0,256])


#showing results
plt.subplot(1,3,1), plt.imshow(img), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(equ_img), plt.title('Global equlization')
plt.subplot(1,3,3), plt.imshow(normalized_img), plt.title('Normalized min-max')
plt.show()

# showing histograms
plt.plot(hist_img), plt.title('Original')
plt.show()
plt.plot(hist_equ_img), plt.title('Global equlization')
plt.show()
plt.plot(hist_normalized_img), plt.title('Normalized min-max')
plt.show()




