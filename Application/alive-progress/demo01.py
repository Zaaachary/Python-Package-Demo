#! -*- encoding:utf-8 -*-
"""
@File    :   demo01.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   $ pip install alive-progress

"""


from alive_progress import alive_bar, config_handler
import time

config_handler.set_global(spinner='message_scrolling', bar='classic')

total = 300
with alive_bar(total) as bar:  # declare your expected total
    for _ in range(total):         # iterate as usual over your items
        time.sleep(2)
        bar()                  # call after consuming one item