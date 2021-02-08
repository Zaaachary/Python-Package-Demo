import cv2
from PIL import Image
import numpy

file_path = 'images/25_1.jpg'

# PIL.Image 2 OpenCV
image = Image.open(file_path)
image.show()

img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV",img)
cv2.waitKey()

# OpenCV 2 PIL.Image
img = cv2.imread(file_path)
cv2.imshow("OpenCV",img)

image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
image.show()
cv2.waitKey()

# 改成两个函数
def PILimg2CVimg(PILimg):
    CVimg = cv2.cvtColor(numpy.asarray(PILimg),cv2.COLOR_RGB2BGR)
    return CVimg

def CVimg2PILimg(CVimg):
    PILimg = Image.fromarray(cv2.cvtColor(CVimg,cv2.COLOR_BGR2RGB))
    return PILimg