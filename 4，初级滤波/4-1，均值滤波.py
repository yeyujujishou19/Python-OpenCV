# coding=utf-8
import cv2

img = cv2.imread("D:/lena.jpg", 0)
result = cv2.blur(img, (5, 5))

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
