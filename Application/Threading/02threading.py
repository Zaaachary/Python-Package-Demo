from time import ctime,sleep
import threading



def coding(func):
    for i in range(3):
        print("I was writing a line of code for %s. %s" % (func,ctime()))
        sleep(2)


def baskating(func):
    for i in range(2):
        print("I just cast a %d-pointer. %s"% (func,ctime()))
        sleep(3)


threads = []
t1 = threading.Thread(target=coding,args=('Otus',))
threads.append(t1)
t2 = threading.Thread(target=baskating,args=(2,))
threads.append(t2)


if __name__ == "__main__":
    print("Class end. %s" % ctime())
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    print("Now I back to study. %s" % ctime())