#!/usr/bin/env python
# coding: utf-8
import numpy as np
import cv2

#可以读取带中文路径的图
def cv_imread(file_path,type=0):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    if(type==0):
        if(len(cv_img.shape)==3):
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    return cv_img


readPath="D:/测试/2.jpg"
image=cv_imread(readPath,type=1)

#将图片存储到带中文的路径里
savePath="D:/测试/3.jpg"
cv2.imencode('.jpg', image)[1].tofile(savePath)