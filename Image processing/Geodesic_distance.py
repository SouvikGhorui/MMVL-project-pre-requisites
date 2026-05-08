# Geodesic distance in image prossecing 
import cv2
import numpy as np
import skimage

def compute_geodesic_dis(img, seed_pt):
    cost_function = img.astype(float)+1.0
    mcp = skimage.graph.MCP_Geometric(cost_function)
    cumulative_costs,_ = mcp.find_costs([seed_pt]) 
    return cumulative_costs


img = np.zeros((500,500))
img[30:70,50:60] = 100

seed = (50,20)

geodesic_dist = compute_geodesic_dis(img, seed)

cv2.imshow('geodesic distance',geodesic_dist)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()