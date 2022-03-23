# Histogram Equalization without using built-in function
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread("lake_nz.jpg")
r,g,b = cv2.split(img)
"""
plt.hist(img)
plt.xlabel('pixel')
plt.ylabel('frequency')
plt.savefig("gray_histogram.png")
"""
def equalize(img):
    a = np.zeros((256,),dtype=np.float16)
    b = np.zeros((256,),dtype=np.float16)
    height,width=img.shape
    #finding histogram
    for i in range(width):
        for j in range(height):
            g = img[j,i]
            a[g] = a[g]+1

    #performing histogram equalization
    tmp = 1.0/(height*width)

    for i in range(256):
        for j in range(i+1):
            b[i] += a[j] * tmp;
        b[i] = round(b[i] * 255);

    # b now contains the equalized histogram
    b=b.astype(np.uint8)

    #Re-map values from equalized histogram into the image
    for i in range(width):
        for j in range(height):
            g = img[j,i]
            img[j,i]= b[g]

    return img

Req = equalize(r)
Geq = equalize(g)
Beq = equalize(b)
eqImg = cv2.merge((Req,Geq,Beq))
cv2.imwrite('equalized.jpg',eqImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
