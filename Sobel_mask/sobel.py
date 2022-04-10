import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")

# Horizontal Sobel Mask
"""[-1-2-1]
   [0 0 0]
   [1 2 1]"""
   
maskH = np.zeros((3,3))
maskH[0] = [-1,-2,-1]
maskH[2] = [1,2,1]

sobelH = cv2.filter2D(img,-1,maskH)
cv2.imwrite('sob_hori.jpg',sobelH)

# Vertical Sobel Mask
"""[-1 0 1]
   [-2 0 2]
   [1 0  1]"""

maskV = np.zeros((3,3))
maskV[0] = [-1,0,1]
maskV[1] = [-2,0,2]
maskV[2] = [1,0,1]
sobelV = cv2.filter2D(img,-1,maskV)
cv2.imwrite('sob_vert.jpg',sobelV)
cv2.destroyAllWindows()