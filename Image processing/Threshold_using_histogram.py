import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# binary threshold
ret , threshold_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

print(ret)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()



#################################################
img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# binary inverse threshold
ret , threshold_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()



####################################################
img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# t
ret , threshold_img = cv2.threshold(img, 150,None, cv2.THRESH_TRUNC)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()


##########################################################

img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# binary threshold
ret , threshold_img = cv2.threshold(img, 150, None, cv2.THRESH_TOZERO)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()

########################################################

img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# binary threshold
ret , threshold_img = cv2.threshold(img, None, 255, cv2.THRESH_OTSU)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()

#########################################################
img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# binary threshold
ret , threshold_img = cv2.threshold(img, None, 255, cv2.THRESH_TRIANGLE)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()

#############################################################
img = cv2.imread('Photos/test_flower.jpg',0)
hist_img = cv2.calcHist([img],[0] , None, [256], [0,255])

# applying different threshold
# binary threshold
ret , threshold_img = cv2.threshold(img, 150, None, cv2.THRESH_TOZERO_INV)

hist_thresh_img = cv2.calcHist([threshold_img],[0] , None, [256], [0,255])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original image')
plt.show()
plt.imshow(cv2.cvtColor(threshold_img, cv2.COLOR_BGR2RGB)), plt.title('Binary threshold image')
plt.show()


plt.plot(hist_img), plt.title(' histogram')
plt.show()
plt.plot(hist_thresh_img), plt.title('Threshold histogram')
plt.show()


 