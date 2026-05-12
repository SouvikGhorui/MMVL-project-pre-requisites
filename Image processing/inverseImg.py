import cv2 
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\MMVL project requirments\Image processing\Photos\test_flower.jpg", cv2.IMREAD_COLOR_RGB)

inverted_img = 255 - img

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(inverted_img)
plt.title("Inverted Image")
plt.axis("off")
plt.show()