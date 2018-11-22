#导入cv模块
import time
import cv2
import os
import sys
from itertools import cycle

# 定义鼠标事件回调函数
def on_mouse(event, x, y, flags, param):

    # 鼠标左键按下，抬起，双击
    if event == cv2.EVENT_LBUTTONDOWN:
        print('左键按下 ({}, {})'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('左键弹起 ({}, {})'.format(x, y))
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('左键双击 ({}, {})'.format(x, y))

    # 鼠标右键按下，抬起，双击
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('右键按下 ({}, {})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        print('右键弹起 ({}, {})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print('右键双击 ({}, {})'.format(x, y))

    # 鼠标中/滚轮键（如果有的话）按下，抬起，双击
    elif event == cv2.EVENT_MBUTTONDOWN:
        print('中间键按下 ({}, {})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONUP:
        print('中间键弹起 ({}, {})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print('中间键双击 ({}, {})'.format(x, y))

    # 鼠标移动
    elif event == cv2.EVENT_MOUSEMOVE:
        print('移动到 ({}, {})'.format(x, y))

# 为指定的窗口绑定自定义的回调函数
cv2.namedWindow('window title')
img = cv2.imread('D:/2.jpg')
cv2.imshow('window title', img)
cv2.setMouseCallback('window title', on_mouse)  # 第一个参数为要绑定的窗口名称，第二个参数为要绑定的鼠标事件
cv2.waitKey()
