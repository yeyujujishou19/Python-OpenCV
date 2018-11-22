# coding=utf-8
import cv2
import numpy as np

img = cv2.imread("D:/test/26.png", 0)

gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(gray_lap) # 转回uint8

cv2.imshow("orign", img)
cv2.imshow('laplacian', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
