# coding=utf-8
import cv2
import numpy as np

image = cv2.imread("D:/test/2.jpg", 0)
lut = np.zeros(256, dtype=image.dtype)  # 创建空的查找表
hist = cv2.calcHist([image],  # 计算图像的直方图
                    [0],  # 使用的通道
                    None,  # 没有使用mask
                    [256],  # it is a 1D histogram
                    [0.0, 255.0])

minBinNo, maxBinNo = 0, 255

# 计算从左起第一个不为0的直方图柱的位置
for binNo, binValue in enumerate(hist):
    if binValue != 0:
        minBinNo = binNo
        break
# 计算从右起第一个不为0的直方图柱的位置
for binNo, binValue in enumerate(reversed(hist)):
    if binValue != 0:
        maxBinNo = 255 - binNo
        break

print(minBinNo, maxBinNo)

# 生成查找表
for i, v in enumerate(lut):
    print
    i
    if i < minBinNo:
        lut[i] = 0
    elif i > maxBinNo:
        lut[i] = 255
    else:
        lut[i] = int(255.0 * (i - minBinNo) / (maxBinNo - minBinNo) + 0.5)

# 计算
result = cv2.LUT(image, lut)
cv2.imshow("Orign", image)
cv2.imshow("Result", result)
cv2.imwrite("LutImage.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
