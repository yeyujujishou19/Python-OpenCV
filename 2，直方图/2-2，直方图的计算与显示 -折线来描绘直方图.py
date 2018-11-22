# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('D:/lena.jpg')
h = np.zeros((256, 256, 3))  # 创建用于绘制直方图的全0图像

bins = np.arange(256).reshape(256, 1)  # 直方图中各bin的顶点位置
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # BGR三种颜色
for ch, col in enumerate(color):
    #cv2.calcHist函数得到的是float32类型的数组
    originHist = cv2.calcHist([img], [ch], None, [256], [0, 256])
    #归一化函数,该函数将直方图的范围限定在0-255×0.9之间。
    cv2.normalize(originHist, originHist, 0, 255 * 0.9, cv2.NORM_MINMAX)

    hist = np.int32(np.around(originHist)) #将整数部分转成np.int32类型
    pts = np.column_stack((bins, hist)) #将直方图中每个bin的值转成相应的坐标
    cv2.polylines(h, [pts], False, col) #根据这些点绘制出折线

h = np.flipud(h) #反转绘制好的直方图，因为绘制时，[0,0]在图像的左上角

cv2.imshow('colorhist', h)
cv2.waitKey(0)
