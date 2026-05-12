import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\MMVL project requirments\Image processing\Photos\test_flower.jpg", cv2.IMREAD_COLOR_RGB)

cropped_image = img[0:790, 0:707]

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(cropped_image)
plt.title("Cropped Image")
plt.axis("off")
plt.show()