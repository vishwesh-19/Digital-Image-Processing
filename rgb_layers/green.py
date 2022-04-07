import cv2
import numpy as np

img = cv2.imread("ireland.jpg")
img[:,:,0] = 0
img[:,:,2] = 0
cv2.imwrite('green.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()