import numpy as np
import pywt
import cv2
# data = np.ones((4,4), dtype=np.float64)

image = cv2.imread("Lenna.png",0)

coeffs = pywt.dwt2(image, 'haar')
cA, (cH, cV, cD) = coeffs
'''print(cA)
print(cV)
print(cD)
'''
cv2.imshow("approximation",np.abs(np.uint8(cA)))
cv2.imshow("horizontal",np.abs(np.uint8(cH)))
cv2.imshow("vertical",np.abs(np.uint8(cV)))
cv2.imshow("diagonal",np.abs(np.uint8(cD)))
cv2.waitKey(0)


# low pass -  approximation subband
# high pass -  detail