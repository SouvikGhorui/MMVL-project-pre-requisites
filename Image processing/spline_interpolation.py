import cv2

img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/photo_1.webp')
w, h, c = img.shape

scale_factor= 2
new_dims = (w*scale_factor,h*scale_factor)

spline_img = cv2.resize(img,new_dims,interpolation=cv2.INTER_CUBIC)

# Results 
cv2.imshow('original',img)
cv2.imshow('Spline interpolation',spline_img)
cv2.waitKey(0)
cv2.destroyAllWindows()