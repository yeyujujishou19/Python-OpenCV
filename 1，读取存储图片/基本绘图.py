#导入cv模块
import cv2 as cv
import numpy as np

# 可以在画面上绘制线段，圆，矩形和多边形等，还可以在图像上指定位置打印文字

import numpy as np
import cv2

# 定义一块宽1600，高1200的画布，初始化为白色
canvas = np.zeros((400, 600, 3), dtype=np.uint8) + 255   #(400, 600, 3) 宽，高，通道

# 画一条纵向的正中央的黑色分界线
cv2.line(canvas, (300, 0), (300, 399), (0, 0, 0), 2)     #(300, 0) 宽，高

# 画一条右半部份画面以199为界的横向分界线
cv2.line(canvas, (300, 199), (599, 199), (0, 0, 0), 2)   #(300, 0) 宽，高

# 左半部分的右下角画个红色的圆
cv2.circle(canvas, (150, 300), 88, (0, 0, 255), 5)       #(80, 300), 100-》圆心，半径

# 左半部分的左下角画个蓝色的矩形
cv2.rectangle(canvas, (10, 300), (50, 390), (255, 0, 0), thickness=3)  #(10, 10), (60, 60) 左上角坐标, 右下角坐标,

# 定义两个三角形，并执行内部绿色填充
triangles = np.array([
    [(150, 240), (95, 333), (205, 333)],
    [(60, 160), (20, 217), (100, 217)]])
cv2.fillPoly(canvas, triangles, (0, 255, 0))

# 画一个黄色五角星
# 第一步通过旋转角度的办法求出五个顶点
phi = 4 * np.pi / 5
rotations = [[[np.cos(i * phi), -np.sin(i * phi)], [i * np.sin(phi), np.cos(i * phi)]] for i in range(1, 5)]
pentagram = np.array([[[[0, -1]] + [np.dot(m, (0, -1)) for m in rotations]]], dtype=np.float)

# 定义缩放倍数和平移向量把五角星画在左半部分画面的上方
pentagram = np.round(pentagram * 80 + np.array([160, 120])).astype(np.int)

# 将5个顶点作为多边形顶点连线，得到五角星
cv2.polylines(canvas, pentagram, True, (0, 255, 255), 9)


# 按像素为间隔从左至右在画面右半部份的上方画出HSV空间的色调连续变化
for x in range(302, 600):
    color_pixel = np.array([[[round(180*float(x-302)/298), 255, 255]]], dtype=np.uint8)
    line_color = [int(c) for c in cv2.cvtColor(color_pixel, cv2.COLOR_HSV2BGR)[0][0]]
    cv2.line(canvas, (x, 0), (x, 197), line_color)


# 如果定义圆的线宽大于半径，则等效于画圆点，随机在画面右下角的框内生成坐标
np.random.seed(42)
n_pts = 30
pts_x = np.random.randint(310, 590, n_pts)   #x范围
pts_y = np.random.randint(210, 390, n_pts)   #y范围
pts = zip(pts_x, pts_y)

# 画出每个点，颜色随机
for pt in pts:
    pt_color = [int(c) for c in np.random.randint(0, 255, 3)]
    cv2.circle(canvas, pt, 3, pt_color, 5)

# 在左半部分最上方打印文字，按此方法不能显示中文
# cv2.putText(canvas,
#             '打印的文字just english',
#             (5, 15),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.5,
#             (0, 0, 0),
#             1)
# cv2.imshow('窗口名称', canvas)
# cv2.waitKey()

# OpenCV-Python在图片上输出中文
# 在Python中，可以借助PIL(Python Imaging Library)模块实现
from PIL import Image, ImageDraw, ImageFont

# 图像从OpenCV格式转换成PIL格式
pil_img = cv2.cvtColor(canvas,cv2.COLOR_BGR2RGB)#cv2和PIL中颜色的hex码的储存顺序不同，需转RGB模式
pilimg = Image.fromarray(pil_img)#Image.fromarray()将数组类型转成图片格式，与np.array()相反
draw = ImageDraw.Draw(pilimg)#PIL图片上打印汉字

#参数1：字体文件路径，参数2：字体大小；Windows系统“simhei.ttf”默认存储在路径：C:\Windows\Fonts中
font = ImageFont.truetype("SIMLI.TTF",30,encoding="utf-8")

draw.text((0,0),"打印的文字 English",(255,0,0),font=font)
cv2img = cv2.cvtColor(np.array(pilimg),cv2.COLOR_RGB2BGR)#将图片转成cv2.imshow()可以显示的数组格式
cv2.imshow("hanzi 汉字",cv2img)  #显示窗口仍然不能显示汉字
cv2.waitKey()
cv2.destroyAllWindows()

