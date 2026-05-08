import numpy as np
from scipy.spatial import distance

img1 = np.array([10,12,3,7,9])
img2 = np.array([3,4,5,6,7])

dist_mink = distance.minkowski(img1, img2,p = 3)
dist_manhattan = distance.minkowski(img1, img2,p=1)

print(f"miskowski distance between image1 and image2 is {dist_mink:.3f}")

print(f"manhattan distance between image1 and image2 is {dist_manhattan:.3f}")