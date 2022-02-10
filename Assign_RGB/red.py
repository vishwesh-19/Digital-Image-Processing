import cv2
import numpy as np

img = cv2.imread("ireland.jpg")
red=img
red[:,:,1]=img[:,:,0]
cv2.imwrite('green.jpg', red)
cv2.waitKey(0)
cv2.destroyAllWindows()