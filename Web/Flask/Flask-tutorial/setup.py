#! -*- encoding:utf-8 -*-
"""
@File    :   setup.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://dormousehole.readthedocs.io/en/latest/tutorial/install.html

# 打包
https://packaging.python.org/tutorials/packaging-projects/

# 在虚拟环境中安装项目
pip install -e .

pip list

至此，没有改变项目运行的方式， FLASK_APP 还是被设置为 flaskr ， 还是使用 flask run 运行应用。不同的是可以在任何地方运行应用，而不仅仅 是在 flask-tutorial 目录下。

"""


from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),   # python 所包括的文件夹
    include_package_data=True,  # 是否包括 .py 之外的文件
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

# 需要 MANIFEST.in 说明文件有哪些 (include_package_data)