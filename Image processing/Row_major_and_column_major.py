import numpy as np
import cv2

img = np.array([[1,2],[3,4]])
row_major = img.flatten(order ='C')
column_major = img.flatten(order='F')

print(f'row_major={row_major}')
print(f'column_major={column_major}')