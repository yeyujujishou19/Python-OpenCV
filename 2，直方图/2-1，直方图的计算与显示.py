import cv2
import numpy as np

#计算并绘制直方图
def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image],
                        [0],  # 使用的通道
                        None,  # 没有使用mask
                        [256],  # HistSize
                        [0.0, 255.0])  # 直方图柱的范围
    #要求矩阵的最小值，最大值，并得到最大值，最小值的索引
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)  #画板
    hpt = int(0.9 * 256);

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)

    return histImg;

if __name__ == '__main__':
    img = cv2.imread("D:/lena.jpg")
    b, g, r = cv2.split(img)  #分离通道

    histImgB = calcAndDrawHist(b, [255, 0, 0]) #绘制直方图
    histImgG = calcAndDrawHist(g, [0, 255, 0])
    histImgR = calcAndDrawHist(r, [0, 0, 255])

    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    # cv2.destroyAllWindows() #注销窗口

