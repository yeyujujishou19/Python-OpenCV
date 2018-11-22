# coding=utf-8
import cv2
import numpy as np

#加入椒盐噪声
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img


img = cv2.imread("D:/lena.jpg", 0)
result = salt(img, 500) #加入椒盐噪声
median = cv2.medianBlur(result, 5)

cv2.imshow("Salt", result)
cv2.imshow("Median", median)

cv2.waitKey(0)
