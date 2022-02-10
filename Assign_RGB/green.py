import cv2
import numpy as np

img = cv2.imread("ireland.jpg")
green=img
green[:,:,2]=img[:,:,0]
cv2.imwrite('green.jpg', green)
cv2.waitKey(0)
cv2.destroyAllWindows()