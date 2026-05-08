import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\Image processing\Photos\photo.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    # Parameters: (source_image, kernel_size, sigmaX)
    # kernel_size must be a tuple of odd numbers, e.g., (5, 5)
    # sigmaX is the standard deviation in the X direction. If 0, it's calculated from the kernel size.
    blurred_light = cv2.GaussianBlur(image, (5, 5), 0)
    blurred_heavy = cv2.GaussianBlur(image, (21, 21), 0)

    # Display the results
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(1, 3, 2), plt.imshow(blurred_light, cmap='gray'), plt.title('Light Blur (5x5 Kernel)')
    plt.subplot(1, 3, 3), plt.imshow(blurred_heavy, cmap='gray'), plt.title('Heavy Blur (21x21 Kernel)')
    plt.show()


