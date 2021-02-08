# -*- coding:utf-8 -*-

import cv2

image = cv2.imread('images/1.jpg')
# cv2.namedWindow("Image1")
cv2.namedWindow("Image2")

# cv2.imshow("Image1", image)


# Canny函数，三个参数：源图像，低阈值，高阈值
image = cv2.Canny(image, 100, 300)
cv2.imshow("Image2", image)

cv2.waitKey(0)
