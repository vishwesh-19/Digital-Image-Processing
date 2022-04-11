import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")

# North Direction/Reference Mask
"""[-1 0 1]
   [-2 0 2]
   [-1 0 1]"""
north = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

# North-West Mask (+45 deg rotation)
"""[0 1 2]
   [-1 0 1]
   [-2-1 0]"""
northW = np.array([[0,1,2],[-1,0,1],[-2,-1,0]])

# West Mask(+90 deg rotation)
"""[1 2 1]
   [0 0 0]
   [-1-2-1]"""  
west = np.zeros((3,3))
west[0] = [1,2,1]
west[2] = [-1,-2,-1]

# South-West Mask
"""[2 1 0]
   [1 0-1]
   [0-1-2]"""
southW = np.array([[2,1,0],[1,0,-1],[0,-1,-2]])

# South Mask
"""[1 0 -1]
   [2 0 -2]
   [1 0 -1]"""
south = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])

# South-East Mask
"""[0-1-2]
   [1 0-1]
   [2 1 0]"""
southE = np.array([[0,-1,-2],[1,0,-1],[2,1,0]])

# East Mask
"""[-1-2-1]
   [0 0 0]
   [1 2 1]"""
east = np.array([[-1,-2,1],[0,0,0],[1,2,1]])

# North-East Mask
"""[-2-1 0]
   [-1 0 1]
   [0 1 2]"""
northE = np.array([[-2,-1,0],[-1,0,1],[0,1,2]])

nF = cv2.filter2D(img,-1,north)
nwF = cv2.filter2D(img,-1,northW)
wF = cv2.filter2D(img,-1,west)
swF = cv2.filter2D(img,-1,southW)
sF = cv2.filter2D(img,-1,south)
seF = cv2.filter2D(img,-1,southE)
eF = cv2.filter2D(img,-1,east)
neF = cv2.filter2D(img,-1,northE)

cv2.imwrite('north.jpg',nF)
cv2.imwrite('northWest.jpg',nwF)
cv2.imwrite('west.jpg',wF)
cv2.imwrite('southWest.jpg',swF)
cv2.imwrite('south.jpg',sF)
cv2.imwrite('southEast.jpg',seF)
cv2.imwrite('east.jpg',eF)
cv2.imwrite('northEast.jpg',neF)
cv2.destroyAllWindows()