import numpy as np

def cosine_similarity(v1,v2):
    product = np.dot(v1,v2)
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)
    cosine_similarity = product/(v1_norm * v2_norm)
    return cosine_similarity
def cosine_difference(v1,v2):
    cosine_dis = 1-cosine_similarity(v1, v2)
    return cosine_dis

def sine_difference(v1,v2):
    sine_diff = (1- cosine_similarity(v1,v2)**2)**(1/2)
    return sine_diff
    
    
u= np.array([10,2,3])
v = np.array([12,4,7])
print(cosine_similarity(u, v))
print(sine_difference(u, v))
