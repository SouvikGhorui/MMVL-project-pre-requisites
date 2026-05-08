import cv2


image = cv2.imread('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/low_const.jpg',1)

# convert BGR to LAB 
lab_img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab_img)

# applying Histogram equalizer to the luminence channel
equ =cv2.equalizeHist(l)
hist_equ_lab = cv2.merge((equ,a,b))
hist_equ_lab = cv2.cvtColor(hist_equ_lab, cv2.COLOR_LAB2BGR)


# Using CLAHE
# create variable for CLAHE
clahe = cv2.createCLAHE(clipLimit = 3.0, tileGridSize=(8,8))
clahe_l_channel = clahe.apply(l)
clahe_img = cv2.merge((clahe_l_channel,a,b))
clahe_img = cv2.cvtColor(clahe_img, cv2.COLOR_LAB2BGR)

cv2.imshow('Original',image)
cv2.imshow('Histogram equalizer',hist_equ_lab)
cv2.imshow('CLAHE',clahe_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



