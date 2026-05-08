from skimage import io, img_as_float, img_as_ubyte


image = io.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\Image processing\Photos\photo_1.webp")
#io.imshow(image)
print(image)
float_img=img_as_float(image)
print("After changing as float")
print(float_img)
print("After changing as integer")
int_img= img_as_ubyte(float_img)
print(int_img)

########################################################################

import cv2
from matplotlib import pyplot as plt

image = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\Image processing\Photos\photo_1.webp")
print(type(image))
# plt.imshow(image) # here matplotlib uses RGB instead of BGR, so values of BLUE are assigned to RED
RGB_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_image)

cv2.imshow("original image",image)
cv2.waitKey(0)
cv2.distroyALLWindows()


