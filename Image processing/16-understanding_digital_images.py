from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float

image = io.imread("Photos/photo.jpg")
#print(image)
#plt.imshow(image)
#print(image.max(),image.min())
'''
# makeing image using random
image_1 = np.random.random([500,500])
print(image_1)
plt.imshow(image_1)
'''

# converting image in float
float_image = img_as_float(image)
plt.imshow(float_image)
print(float_image.max(),float_image.min())

# creating black image using zero matrix
Dark_image = np.zeros((500,500,3))
plt.imshow(Dark_image)


Dark_image[100:400,100:400] = (250,0,0)
plt.imshow(Dark_image)

