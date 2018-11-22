import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('D:/lena.jpg')
bins = np.arange(257)

item = img[:, :, 1]
hist, bins = np.histogram(item, bins)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
