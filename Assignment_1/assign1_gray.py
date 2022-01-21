# Assignment 1 : Convert image to grayscale without built-in function

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Lenovo\\Documents\\6th_sem\\Digital_IP\\vj.jpg")
print(np.shape(img))
print(type(img[0][0][0]))
#shape [826, 611, 3]
gray = np.zeros([826, 611], dtype=np.uint8)
for i in range(0,826):
    for j in range(0, 611):
        s = 0
        for k in range(0,3):
            s += img[i][j][k]
        gray[i][j] = s/3
        
cv2.imwrite('vj_gray.jpg',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()