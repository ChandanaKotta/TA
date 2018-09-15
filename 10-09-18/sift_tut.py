import cv2
from siftdetector import detect_keypoints



img1 = cv2.imread('iiitb.jpg',cv2.COLOR_BGR2GRAY) # queryImage
[keypoints, descriptors] = detect_keypoints(imagename, 15)
cv2.imshow("a",keypoints)
cv2.waitKey(0)