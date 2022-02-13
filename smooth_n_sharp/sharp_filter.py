import cv2
import numpy as np

img = cv2.imread("lake_nz.jpg")
# Laplacian Filters
# [(1,1,1),(1,-8,1),(1,1,1)]
mask1 = np.ones([3,3], dtype=int)
mask1[1][1] = -8

# [(0,1,0),(1,-4,1),(0,1,0)]
mask2 = np.zeros([3,3], dtype=int)
mask2[1][1] = -4
mask2[1][0]=mask2[0][1]=mask2[2][0]=mask2[0][2]=1

def filter(img1, mask):
    m, n = img1.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = img1[i-1, j-1]*mask[0, 0]+img1[i-1, j]*mask[0, 1]+img1[i-1, j + 1]*mask[0, 2]+img1[i, j-1]*mask[1, 0]+ img1[i, j]*mask[1, 1]+img1[i, j + 1]*mask[1, 2]+img1[i + 1, j-1]*mask[2, 0]+img1[i + 1, j]*mask[2, 1]+img1[i + 1, j + 1]*mask[2, 2]
            img_new[i, j]= temp
    return img_new


r,g,b = cv2.split(img)

R1 = filter(r, mask1); G1 = filter(g, mask1); B1 = filter(b, mask1)
sharp1 = cv2.merge((R1,G1,B1))

R2 = filter(r, mask1); G2 = filter(g, mask1); B2 = filter(b, mask1)
sharp2 = cv2.merge((R2,G2,B2))

cv2.imshow('', sharp1)
cv2.waitKey(0)
cv2.imshow('', sharp2)
cv2.waitKey(0)
cv2.destroyAllWindows()