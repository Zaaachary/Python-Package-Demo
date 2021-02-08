# -*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

# drawHist
def drawHist(image):
    # 图像直方图
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.figure()  # 新建一个图像
    plt.title("Grayscale Histogram")  # 图像的标题
    plt.xlabel("Bins")  # X轴标签
    plt.ylabel("# of Pixels")  # Y轴标签
    plt.plot(hist)  # 画图
    plt.xlim([0, 256])  # 设置x坐标轴范围
    plt.show()  # 显示图像

# read image
image = cv2.imread("images/25_1.jpg", 0)
cv2.imshow("image", image)
drawHist(image)


# equalize Hist方法 直方图均衡化
eq = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization", eq)
# cv2.imshow("Histogram Equalization", np.hstack([eq]))
drawHist(eq)

cv2.waitKey(0)
