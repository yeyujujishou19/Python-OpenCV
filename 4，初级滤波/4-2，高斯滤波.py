# coding=utf-8
import cv2

img = cv2.imread("D:/lena.jpg", 0)
gaussianResult = cv2.GaussianBlur(img,(5,5),1.5)

cv2.imshow("Origin", img)
cv2.imshow("GaussianBlur", gaussianResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
