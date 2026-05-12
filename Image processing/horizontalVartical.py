import cv2 
import matplotlib.pyplot as plt  

img = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\MMVL project requirments\Image processing\Photos\test_flower.jpg", cv2.IMREAD_COLOR_RGB)

h_flip = cv2.flip(img, 1)
v_flip = cv2.flip(img, 0)
mix_flip = cv2.flip(img, -1)

plt.figure(figsize = (20, 5))
plt.subplot(1, 4, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 4, 2)
plt.imshow(h_flip)
plt.title("Horizontal Flip")
plt.axis("off")
plt.subplot(1, 4, 3)
plt.imshow(v_flip)
plt.title("Vertical Flip")
plt.axis("off")
plt.subplot(1, 4, 4)
plt.imshow(mix_flip)
plt.title("Mix Flip")
plt.axis("off")
plt.show()