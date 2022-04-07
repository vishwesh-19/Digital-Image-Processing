import cv2
import numpy as np

img = cv2.imread("ireland.jpg")
img[:,:,0]=0
img[:,:,1]=0
cv2.imwrite('red.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()