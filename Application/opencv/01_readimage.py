# -*- coding:utf-8 -*-
'''读取一张图片，并显示出来'''
import cv2
# 根据路径读取一张图片
file_path = "'D:/Media/图片/壁纸/书签.jpg'"

image = cv2.imread("images/test2.jpg")
# 初始化一个窗口
cv2.namedWindow("Image1")
# 显示图片
cv2.imshow("Image1", image)
# 等待键盘触发事件，释放窗口
cv2.waitKey(0)


