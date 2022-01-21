import cv2
import numpy as np

img = cv2.imread("ireland.jpg")
sum_pix = np.zeros([148, 200, 3], dtype=np.uint8)

print(np.shape(img))  
for i in range(0,148):
    for j in range(0,200):
        for k in range(0,3):
            sum_pix[i][j][k] = img[i][j][k] + 100   # Addition
cv2.imwrite('add.jpg', sum_pix)        
cv2.waitKey(0)
cv2.destroyAllWindows()