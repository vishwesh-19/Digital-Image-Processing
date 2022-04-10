import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")

# Horizontal Prewitt Mask
# [(-1 -1 -1),(0,0,0),(1,1,1)]
Mx = np.ones((3,3))
for i in range(3):
    Mx[i,:] = i-1
pH = cv2.filter2D(img,-1,Mx)
cv2.imwrite('prewitt_hori.jpg',pH)
cv2.waitKey(0)

# Vertical Prewitt Mask
# [(-1 0 1),(-1 0 1),(-1 0 1)]
My = np.ones((3,3))
for i in range(3):
    My[:,i] = i-1
pV = cv2.filter2D(img,-1,My)
cv2.imwrite('prewitt_vert.jpg',pV)
cv2.destroyAllWindows()