# Histogram Equalization using built-in function
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lake_nz.jpg")
r,g,b = cv2.split(img)

""" 
1. Function works only on 2d arrays/grayscale images.
2. Therefore we equalize 3 layers of the image and merge them to get equalization of 
   original coloured image. 
"""
   
R = cv2.equalizeHist(r)
G = cv2.equalizeHist(g)
B = cv2.equalizeHist(b)

# Merging R,G,B to get colour image
histEq = cv2.merge((R,G,B))

# Getting frequency of each unique pixel value
pix, freq = np.unique(img, return_index=True)
Eq_pix, Eq_freq = np.unique(histEq, return_index=True)

cv2.imwrite('equalize1.jpg', histEq)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(pix, freq)
plt.xlabel('pixel')
plt.ylabel('frequency')
plt.savefig('colorImg.png')

plt.plot(Eq_pix, Eq_freq)
plt.xlabel('pixel')
plt.ylabel('frequency')
plt.savefig('equalized_color.png')