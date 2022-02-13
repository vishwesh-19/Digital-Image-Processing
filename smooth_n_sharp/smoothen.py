import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")
fil = np.ones((3,3),np.float32)/9
smooth = cv2.filter2D(img,-1,fil)

cv2.imshow('', smooth)
cv2.waitKey(0)
cv2.destroyAllWindows()

# On increasing the filter size, image gets more diffused 