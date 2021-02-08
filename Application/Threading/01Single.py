from time import ctime,sleep


def coding(func):
    for i in range(2):
        sleep(1)
        print("I just wrote a line of code for %s. %s" % (func,ctime()))


def baskating(func):
    for i in range(3):
        sleep(2)
        print("I just cast a %d-pointer. %s"% (func,ctime()))
        sleep(2)


if __name__ == "__main__":
    print("Class end. %s" % ctime())
    coding('Otus algorithm')
    baskating(3)
    print("Now I back to study. %s" % ctime())