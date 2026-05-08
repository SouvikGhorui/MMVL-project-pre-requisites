import cv2
from skimage import exposure
import matplotlib.pyplot as plt

source = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/source.jpg')
reference = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/reference.webp')

matched_img = exposure.match_histograms(source, reference, channel_axis = -1)

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
plt.title('Original')


plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(reference, cv2.COLOR_BGR2RGB))
plt.title('Reference')


plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(matched_img, cv2.COLOR_BGR2RGB))
plt.title('Histogram matching')
plt.show()



