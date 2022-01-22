import cv2
import numpy as np

img = cv2.imread("ireland.jpg")
r = cv2.selectROI(img)
print(r)
img1 = img
for i in range(r[1],r[3]):
    for j in range(r[0],r[2]):
        for k in range(0,3):
            img1[i][j][k]=0
cv2.imwrite('blk.jpg', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#crop = np.zeros([r[3]-r[1], r[2]-r[0], 3], dtype=np.uint8)