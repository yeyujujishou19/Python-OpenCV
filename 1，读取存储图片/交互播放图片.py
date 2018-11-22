#导入cv模块
import time
import cv2
import os
import sys
from itertools import cycle

# =====================OpenCV窗口显示===============================

# img = cv2.imread('D:/test/1.jpg')
# cv2.imshow('窗口标题', img)
# cv2.waitKey()

# =====================OpenCV窗口循环===============================

frame_path="D:/test"  # 图片的文件夹路径

# 列出frames文件夹下的所有图片
filenames = os.listdir(frame_path)

# 通过itertools.cycle生成一个无限循环的迭代器，每次迭代都输出下一张图像对象
img_iter = cycle([cv2.imread(os.sep.join([frame_path, x])) for x in filenames])

key = 0
while key & 0xFF != 27:
    cv2.imshow('window title', next(img_iter))
    key = cv2.waitKey(1000)  #1000为间隔1000毫秒 cv2.waitKey()参数不为零的时候则可以和循环结合产生动态画面
