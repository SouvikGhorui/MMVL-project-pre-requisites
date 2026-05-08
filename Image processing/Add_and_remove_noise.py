import numpy as np
import matplotlib.pyplot as plt
import cv2

def salt_and_paper(img,noise_size):
    img_copy = img.copy()
    row,col = img_copy.shape
    for i in range(noise_size):
        x,y = np.random.randint(0,row), np.random.randint(0,col)
        if np.random.random()<0.5:
            img_copy[x,y] = 0
        else:
            img_copy[x,y]=255
    return img_copy
img = cv2.imread('Photos/test_flower.jpg',0)

noise_img = salt_and_paper(img,5000)
denoise_img = cv2.medianBlur(noise_img, 3)

'''
plt.imshow(cv2.cvtColor(noise_img, cv2.COLOR_BGR2RGB))
plt.show()
'''

cv2.imshow('Original',img)
cv2.imshow('noise image',noise_img)
cv2.imshow('denoise imge',denoise_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#############################################

def gaussian_noise(img,mean, std_deviation):
    row, col = img.shape
    gauss = np.random.normal(mean, std_deviation, (row, col))
    noisy_img = gauss + img
    noisy_img = np.clip(noisy_img,0,255)
    return noisy_img.astype(np.uint8)

gaussian_noise_img=gaussian_noise(img, 0, 25)

median_removal = cv2.medianBlur(gaussian_noise_img, 3)
gaussian_blur_img = cv2.GaussianBlur(gaussian_noise_img, (3,3), 0)
nl_denoising = cv2.fastNlMeansDenoising(gaussian_blur_img,None,h =10, templateWindowSize = 7, searchWindowSize = 21)

cv2.imshow('Gaussian noise image',gaussian_noise_img)
cv2.imshow('After using Non local mean method',nl_denoising)
cv2.imshow('After using Gaussian blur',gaussian_blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
###################################################33
import numpy as np
import matplotlib.pyplot as plt
import cv2
def add_spectral_noise(img):
    row, col = img.shape
    gauss = np.random.randn(row,col)
    gauss = gauss.reshape(row, col)
    noise_img = img + img*gauss * 0.5
    noise_img = np.clip(noise_img, 0, 255)
    return noise_img.astype(np.uint8)

img = cv2.imread('Photos/test_flower.jpg',0)
spectral_noise_img = add_spectral_noise(img)

# removing noise 
gaussian_blur_img = cv2.GaussianBlur(spectral_noise_img, (3,3), 0)
bilateral_img = cv2.bilateralFilter(spectral_noise_img, 9, 75, 75)
cv2.imshow('spectral noise', spectral_noise_img)
cv2.imshow('Gaussian blured image',gaussian_blur_img)
cv2.imshow('Bilateral filtered image', bilateral_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
     
    