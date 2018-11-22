# coding=utf-8
import cv2

img = cv2.imread("D:/test/2.jpg",0)
equ = cv2.equalizeHist(img)
cv2.imshow('equ',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
