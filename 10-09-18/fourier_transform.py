'''
Author:Chandana Kotta 
(Original Code)

'''

from glob import glob
import numpy as np
# import radialProfile
import cv2
import matplotlib.pyplot as plt

def fft(image):
	fft = np.fft.fft2(image)
	fshift = np.fft.fftshift(fft)
	phase = np.angle(fshift)
	magnitude = 10*np.log(np.abs(fshift))
	return magnitude, phase	

image = cv2.imread("Lenna.png",0)

magnitude1, phase1 = fft(np.uint8(image))

cv2.imshow("magnitude",np.abs(np.uint8(magnitude1)))
cv2.imshow("phase",phase1)
cv2.waitKey(0)



