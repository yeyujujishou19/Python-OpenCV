# coding=utf-8
import cv2
import numpy as np

#开运算和闭运算就是将腐蚀和膨胀按照一定的次序进行处理。
# 但这两者并不是可逆的，即先开后闭并不能得到原先的图像。

img = cv2.imread('D:/test/1.png', 0)

cv2.imshow("Orign Image", img);

# 定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

# 闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 显示腐蚀后的图像
cv2.imshow("Close", closed);

# 开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 显示腐蚀后的图像
cv2.imshow("Open", opened);

cv2.waitKey(0)
cv2.destroyAllWindows()
