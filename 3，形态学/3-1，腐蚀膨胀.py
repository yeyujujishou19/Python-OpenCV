# coding=utf-8
import cv2
import numpy as np

# opencv里所说的腐蚀，膨胀是针对白色区域，腐蚀是缩小白色区域，膨胀是扩大白色区域

img = cv2.imread("D:/test/3.jpg", 0)
# OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (27, 27))
cv2.imshow("Orign Image", img);
# 腐蚀图像
eroded = cv2.erode(img, kernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded Image", eroded);

# 膨胀图像
dilated = cv2.dilate(img, kernel)
# 显示膨胀后的图像
cv2.imshow("Dilated Image", dilated);
# 原图像
cv2.imshow("Origin", img)

# NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3, 3)))
Nperoded = cv2.erode(img, NpKernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded by NumPy kernel", Nperoded);

cv2.waitKey(0)
cv2.destroyAllWindows()
