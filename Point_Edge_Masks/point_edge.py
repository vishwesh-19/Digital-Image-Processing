import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")

# Point Detection Mask
point_mask = np.ones((3,3))
point_mask[1,1] = -8

point = cv2.filter2D(img,-1,point_mask)
cv2.imwrite('point.jpg',point)

# Edge Detection Masks

# Horizontal Mask
edge_mask1 = -1*np.ones((3,3))
for i in range(3):
    edge_mask1[1,i] = 2
edge1 = cv2.filter2D(img,-1,edge_mask1)
cv2.imwrite('horizontalEdge.jpg',edge1)

# Vertical Mask
edge_mask2 = -1*np.ones((3,3))
for i in range(3):
    edge_mask2[i,1] = 2   
edge2 = cv2.filter2D(img,-1,edge_mask2)
cv2.imwrite('verticalEdge.jpg',edge2)

# Diagonal Mask
edge_mask3 = -1*np.ones((3,3))
for i in range(3):
    edge_mask3[i,i] = 2
edge3 = cv2.filter2D(img,-1,edge_mask3)
cv2.imwrite('diagonalEdge.jpg',edge3)
cv2.destroyAllWindows()