# importing packages
from skimage.exposure import match_histograms
import cv2

# loading data
reference = cv2.imread("ireland.jpg")
image = cv2.imread("lake_nz.jpg")

# matching histograms
matched = match_histograms(image, reference,
						multichannel=True,)

cv2.imwrite('matched.png',matched)
cv2.waitKey(0)
cv2.destroyAllWindows()