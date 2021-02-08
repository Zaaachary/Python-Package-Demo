# -*- coding:utf-8 -*-
'''读取'''

import cv2

# 返回值为一个矩阵
image = cv2.imread('images/classr.jpg')

cv2.namedWindow("Imageo")
cv2.namedWindow("Imagec")

def opcvnumpy():
    # numpy.array item函数，可访问矩阵中特定通道的像素值
    # 参数:x,y,通道
    print(image.item(150, 120, 2))

    # itemset() 函数可设定像素值
    # 参数: 三元组（x,y,通道）,设定的像素值
    image.itemset((150, 120, 2), 255)

    # 输出新的像素值
    print(image.item(150, 120, 2))


def setzero():
    cv2.imshow("Imageo",image)
    # 获取所有行列的全部像素， 1是BGR中的G
    image[:,:,1] = 0
    cv2.imshow("Imagec", image)


def black():
    cv2.imshow("Imageo",image)
    # 设置100,100 到200,350为感兴趣区域
    roi = image[100:200, 100:350]
    # 将roi区域内所有像素设置为0,0表示黑色
    roi[:] = 0
    cv2.imshow("Imagec",image)

def copy():
    cv2.imshow("Imageo",image)
    roi = image[0:100, 0:100]  # 设置感兴趣区域

    # 将感兴趣区域的像素复制给(200, 200)到(300, 300)的正方形区域
    # 两个区域的大小需要相同，大小不仅包括长宽，还要求通道数也相等
    image[200:300, 200:300] = roi

    cv2.imshow("Imagec", image)



# setzero();
# black();
copy()

cv2.waitKey(0)



