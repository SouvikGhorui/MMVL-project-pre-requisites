
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/photo_1.webp',cv2.IMREAD_GRAYSCALE)

# cv2.calcHist(images, channels, mask, histSize, ranges)
# images: Source image (in brackets)
# channels: Index of channel ([0] for grayscale)
# mask: None (unless you want to find hist of a specific region)
# histSize: How many bins ([256])
# ranges: Pixel value range ([0, 256])
hist = cv2.calcHist([image], [0],None, [256], [0,256])

# display results
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title('Original image',)

plt.subplot(1,2,2)
plt.plot(hist)
plt.xlabel('Pixel intensity')
plt.ylabel('No. of pixel')
plt.title('Histogram')
plt.show()

######
# Histogram for coloured image

image = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/photo_1.webp',cv2.IMREAD_COLOR_RGB)


# display results
plt.subplot(1,2,1)
plt.imshow(image)
plt.title('Original image')

plt.subplot(1,2,2)
colors = ['b','g','r']
for i in range(len(colors)):
    hist = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist,colors[i])
plt.xlabel('Pixel intensity')
plt.ylabel('No. of pixel')
plt.title('Histogram')
plt.show()