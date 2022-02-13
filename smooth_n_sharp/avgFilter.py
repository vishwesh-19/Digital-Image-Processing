import cv2
import numpy as np
  
     
# Read the image
img = cv2.imread("lake_nz.jpg")
r, g, b = cv2.split(img)
# Obtain number of rows and columns
# of the image
  
# Develop Averaging filter(3, 3) mask
mask = np.ones([3, 3], dtype = int)
mask = mask / 9
  
# Convolve the 3X3 mask over the image
def filter(img1):
    m, n = img1.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = img1[i-1, j-1]*mask[0, 0]+img1[i-1, j]*mask[0, 1]+img1[i-1, j + 1]*mask[0, 2]+img1[i, j-1]*mask[1, 0]+ img1[i, j]*mask[1, 1]+img1[i, j + 1]*mask[1, 2]+img1[i + 1, j-1]*mask[2, 0]+img1[i + 1, j]*mask[2, 1]+img1[i + 1, j + 1]*mask[2, 2]
            img_new[i, j]= temp
    return img_new

red = filter(r)
green = filter(g)
blue = filter(b)

filtered = cv2.merge((red, green, blue))
filtered = filtered.astype(np.uint8)
cv2.imwrite('avgFilter.jpg', filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()