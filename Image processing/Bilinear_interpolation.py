import cv2
img = cv2.imread('Photos/test_flower.jpg')

scale_factor = 0.5
w, h, c = img.shape
new_dims = (int(w* scale_factor),int(h * scale_factor))

# bilinear interpolation (best for downscaling image)
bilinear_img = cv2.resize(img,new_dims,interpolation = cv2.INTER_LINEAR)

#results
cv2.imshow('Original',img)
cv2.imshow('Bilinear interpolation',bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

