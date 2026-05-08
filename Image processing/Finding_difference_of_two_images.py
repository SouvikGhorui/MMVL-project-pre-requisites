from skimage.metrics import structural_similarity as ssim
import cv2

img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/photo.jpg',cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/photo_1.webp',cv2.IMREAD_GRAYSCALE)
height,weight =img.shape
img1 = cv2.resize(img1,(weight, height))
# findig difference score and difference image using ssim
(score, diff_ssim) = ssim(img,img1,full=True)
diff_ssim = (diff_ssim*255).astype("uint8")

print(f"Score of similarity {score: 0.4f}")
theshold, diff_theshold_ssim =cv2.threshold(diff_ssim, 0, 255, cv2.THRESH_BINARY_INV) 

cv2.imshow("difference image",diff_ssim)
cv2.imshow("difference theshold", diff_theshold_ssim)

cv2.waitKey(0)
cv2.destroyAllWindows()

    
    
    


