import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")
# Robert's Filter
# [(-1 0),(0 1)]
rob = np.zeros((2,2))
for i in range(2):
    rob[0,0] = -1
    rob[1,1] = 1
rF = cv2.filter2D(img,-1,rob)
cv2.imwrite('robert.jpg',rF)
cv2.waitKey(0)
cv2.destroyAllWindows()