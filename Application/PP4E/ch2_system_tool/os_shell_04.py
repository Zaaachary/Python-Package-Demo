import os

print(os.popen('type os_shell_04.py').read())

List = os.popen('dir /B').readlines()
print(List)

print('\n[os_03.py]')   
os.system('python os_03.py')        # 运行一个Python程序

output = os.popen('python os_03.py').read()     # 运行并获取输出
print('\n[os_03.py]', output)