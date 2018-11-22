# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('D:/lena.jpg')
h = np.zeros((300, 256, 3))
bins = np.arange(257)
bin = bins[0:-1]
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

for ch, col in enumerate(color):
    item = img[:, :, ch]
    N, bins = np.histogram(item, bins)
    v = N.max()
    N = np.int32(np.around((N * 255) / v))
    N = N.reshape(256, 1)
    pts = np.column_stack((bin, N))
    cv2.polylines(h, [pts], False, col)

h = np.flipud(h)

cv2.imshow('image', h)
cv2.waitKey(0)
