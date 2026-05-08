import cv2
from matplotlib import pyplot as plt


image = cv2.imread('Photos/photo.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# to remove noise, we use gaussian blur method
blur = cv2.GaussianBlur(image, (3,3), 0)

# using Otsu thresold
ret , mask = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# to extract the foreground using mask
#bitwise and keeps the pixel where the mask is white
foreground = cv2.bitwise_and(image, image,mask = mask)

# Display result
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title('Original image')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(foreground,cv2.COLOR_BGR2RGB))
plt.title('Segmentation foreground')

