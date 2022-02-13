# Binarization/Thresholding of Image
# Pixel having value >= threshold, pixel value = 255 (white)
# else pixel value = 0 (black)
import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(np.shape(gray))      Output (500, 740)

cv2.imwrite('gray.jpg', gray)
cv2.waitKey(0)

T = 100      # Threshold
for i in range(0,500):
    for j in range(0, 740):
        if(gray[i][j] >= T):
            gray[i][j] = 255
        else:
            gray[i][j] = 0

cv2.imwrite('binary.jpg', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()