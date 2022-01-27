import cv2
import numpy as np

rect = cv2.imread("rectangle.png")
circle = cv2.imread("circle.png")

And = cv2.bitwise_and(rect, circle)    # Bitwise AND
Nand = cv2.bitwise_not(And)            # Bitwise NAND

Or = cv2.bitwise_or(rect, circle)      # Bitwise OR
Nor = cv2.bitwise_not(Or)              # Bitwise Nor

notRect = cv2.bitwise_not(rect)        # Bitwise NOT
notCircle = cv2.bitwise_not(circle)

Xor = cv2.bitwise_xor(rect,circle)     # Bitwise XOR
Xnor = cv2.bitwise_not(Xor)            # Bitwise XNOR

cv2.imwrite("and.jpg", And)
cv2.imwrite("nand.jpg", Nand)
cv2.imwrite("or.jpg", Or)
cv2.imwrite("nor.jpg", Nor)
cv2.imwrite("notRect.jpg", notRect)
cv2.imwrite("notCircle.jpg", notCircle)
cv2.imwrite("xor.jpg", Xor)
cv2.imwrite("xnor.jpg", Xnor)
cv2.waitKey(0)
cv2.destroyAllWindows()