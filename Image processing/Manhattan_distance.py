# mathattan distance metric

import numpy as np


def calculate_l1_distance(image_a, image_b):
    image_a = image_a.astype('float')
    image_b = image_b.astype('float')
    diff = np.abs(image_a - image_b)
    total_distance = np.sum(diff)
    return total_distance
img1 = np.random.randint(0,255,(5,5), dtype = np.uint8)
img2 = np.random.randint(0,255, (5,5), dtype = np.uint8)

score = calculate_l1_distance(img1, img2)
print(f'Score = {score}')



