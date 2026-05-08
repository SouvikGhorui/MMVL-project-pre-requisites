import cv2
from skimage.filters import roberts, sobel, farid, scharr, prewitt

image = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\Image processing\Photos\photo_1.webp", 0)


if image is None:
    print("Error: Image not found. Check the path.")
else:
    roberts_img = roberts(image)
    sobel_img = sobel(image)
    scharr_img = scharr(image)

    farid_img = farid(image) 
    prewitt_img = prewitt(image)

    cv2.imshow("Roberts image", roberts_img)
    cv2.imshow("Sobel image", sobel_img)
    cv2.imshow("Scharr image", scharr_img)
    cv2.imshow("Farid image", farid_img)
    cv2.imshow("Prewitt image", prewitt_img)

    cv2.waitKey(0)
    
    
    cv2.destroyAllWindows()
    

###########################################################################
import cv2

image = cv2.imread(r"C:\Users\sghor\Desktop\Souvik\Programming\Image processing\Photos\photo_1.webp", 0)
canny_edge = cv2.Canny(image,50,180)
cv2.imshow("Canny edge delection",canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()