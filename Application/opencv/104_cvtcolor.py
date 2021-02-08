import cv2
from PIL import Image
import numpy as np
#-------------------------------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg
#------------------------------------------------------------------------------------------

def PIL_img2CV_img(PILimg):
    CVimg = cv2.cvtColor(np.asarray(PILimg), cv2.COLOR_RGB2BGR)
    return CVimg

def CV_img2PIL_img(CVimg):
    PILimg = Image.fromarray(cv2.cvtColor(CVimg, cv2.COLOR_BGR2RGB))
    return PILimg

mpl.rcParams['font.sans-serif'] = ['SimHei']  #中文显示
mpl.rcParams['axes.unicode_minus']=False      #负号显示

def drawHist(image):
    # 图像直方图
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    f = plt.figure()  # 新建一个图像
    plt.title("Grayscale Histogram")  # 图像的标题
    plt.xlabel("Bins")  # X轴标签
    plt.ylabel("# of Pixels")  # Y轴标签
    plt.plot(hist)  # 画图
    plt.xlim([0, 256])  # 设置x坐标轴范围
    # plt.show()  # 显示图像


# cvimg = cv2.imread('images/1.jpg',1)
pilimg = Image.open('images/1.jpg')
cvimg = PIL_img2CV_img(pilimg)


gray = cv2.cvtColor(cvimg,cv2.COLOR_BGR2GRAY)
CV_img_eq = cv2.equalizeHist(gray)
# cv2.namedWindow("Image2")
# cv2.imshow("Image2", CV_img_eq)





# img_re = cv2.cvtColor(CV_img_eq,cv2.COLOR_GRAY2BGR)
# cv2.namedWindow("Image1")
# cv2.imshow("Image1", img_re)

cv2.waitKey(0)