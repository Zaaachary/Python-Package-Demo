import sys
print(sys.path)

# 在程序运行过程中修改
sys.path.append('D:\CODE\Python-Packages-Demo\PP4E')

from more_01 import more
more('\n'.join(sys.path))

# exc_info
try:
    raise IndexError
except:
    print(sys.exc_info())

# traceback模块
import traceback
traceback.print_tb(sys.exc_info()[2])