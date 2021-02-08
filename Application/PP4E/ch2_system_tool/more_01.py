"""
split and interactively page a string or file of text
使用方法：
e.g. 
// 在 Python 解释器中引入
import sys
from more_01 import more
more(sys.__doc__)

// 在命令行中 作为程序运行，将文件名作为参数
> python more.py xxx.py 
"""

def more(text, numlines=15):
    lines = text.splitlines()                   # 比 split('\n') 少了最后空白字符串
    while lines:
        chunk = lines[:numlines]                # 默认一次15行
        lines = lines[numlines:]                # 保存15行后的内容
        for line in chunk: print(line)
        if lines and input('More? Y/N') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys                                  # 不在导入时执行，仅运行时
    more(open(sys.argv[1], 'r', encoding='utf-8').read(), 10)          # 打开命令行内输入的文件，并输出内容
