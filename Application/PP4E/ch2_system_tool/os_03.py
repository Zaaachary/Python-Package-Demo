import os

# 文件/目录
print('isfile:', os.path.isfile(r'.\more_01.py'))  # 是否存在且为文件

print('isdir:', os.path.isdir(r'.\pathTestDir'))  # 是否存在切为目录

print('exists:', os.path.exists(r'.\os_03.py'))    # 是否存在

print('getsize', os.path.getsize(r'.\os_03.py'))   # 返回大小

# 路径
print('split:', os.path.split(r'D:\CODE\test.txt'))   # 路径、文件名

print('join:', os.path.join(r'D:\CODE','test.txt'))  # 在命令行中输出的是'D:\\CODE\\test.txt'

name = r'D:\CODE\Python-Packages-Demo\PP4E\os_03.py'
print('dirname, basename:', os.path.dirname(name),',', os.path.basename(name))

print('splitext:', os.path.splitext(name))   # 分离出扩展名