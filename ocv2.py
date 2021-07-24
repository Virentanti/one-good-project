import cv2
import numpy as np

img= cv2.imread("ques.png")

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#orange= np.uint8([[[0,255,255]]])
lower_orange= np.array([14,18,100])
upper_orange= np.array([14,87,100])
mask= cv2.inRange(hsv, lower_orange, upper_orange)
res= cv2.bitwise_and(img, img, mask = mask)


cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("res", res)
cv2.waitKey(0)

