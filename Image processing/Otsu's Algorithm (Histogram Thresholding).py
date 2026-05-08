import cv2

img = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/small_test_flower.jpg',0)

ret, thesh_img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

#resulting images
cv2.imshow('Theshold image',thesh_img)
cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()