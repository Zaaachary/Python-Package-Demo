import time
import threading

# 原始代码
# def foo():
#     time.sleep(2)   #程序休息2秒
#     print("ok",time.ctime())

# for i in range(20):
#     t1=threading.Thread(target=foo,args=()) #实例化一个线程
#     t1.start()  #启动线程
# 如果在主机执行IO密集型任务的时候再执行这种类型的程序时，计算机就有很大可能会宕机。



# 这时候就可以为这段程序添加一个计数器功能，来限制一个时间点内的线程数量。

s1=threading.Semaphore(5)   #添加一个计数器

def foo():
    s1.acquire()    #计数器获得锁
    time.sleep(2)   #程序休眠2秒
    print("ok",time.ctime())
    s1.release()    #计数器释放锁

if __name__ == "__main__":
    for i in range(30):
        t1=threading.Thread(target=foo,args=()) #创建线程
        t1.start()  #启动线程   