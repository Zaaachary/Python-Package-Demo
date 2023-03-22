# -*- encoding: utf-8 -*-
'''
@File    :   1_coroutines_and_task.py
@Time    :   2023/03/22 11:00:22
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@outlook.com
@Desc    :   
'''

import asyncio
import time


# coroutines 协程

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main_1():
    # run one by one
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

print("main 1 sequential")
asyncio.run(main_1())

async def main_2():
    # run 
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

print("main 2 concurrency")
asyncio.run(main_2())

# Promise object

async def nested():
    return 42

async def main_3():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # try:
    nested()        # warning
    # except:
        # ...

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

print('main 3 Promise object')
asyncio.run(main_3())

# task
# 当一个协程通过 asyncio.create_task() 等函数被封装为一个 任务，该协程会被自动调度执行:

async def main_4():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)

print('main 4 task')
asyncio.run(main_4())

# Futures

'''
Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:

async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
一个很好的返回对象的低层级函数的示例是 loop.run_in_executor()。
'''

# 运行程序

'''
此函数会运行传入的协程，负责管理 asyncio 事件循环，终结异步生成器，并关闭线程池。

当有其他 asyncio 事件循环在同一线程中运行时，此函数不能被调用。

如果 debug 为 True，事件循环将以调试模式运行。

此函数总是会创建一个新的事件循环并在结束时关闭之。它应当被用作 asyncio 程序的主入口点，理想情况下应当只被调用一次。
'''

async def main_5(i=1):
    await asyncio.sleep(i)
    print('hello')

print('main 5')
asyncio.run(main_5())

# 创建任务
background_tasks = set()

async def main_6():

    # loop = asyncio.get_event_loop()

    for i in range(10, -1, -1):
        task = asyncio.create_task(main_5(i=i))

        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task.add_done_callback(background_tasks.discard)

    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(*background_tasks)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_6())


# 并发运行任务
'''
asyncio gather
并发 运行 aws 序列中的 可等待对象。
如果 aws 中的某个可等待对象为协程，它将自动被作为一个任务调度。
如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。
如果 return_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。
如果 return_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。
如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一样处理 -- 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。
'''
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main_7():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main_7())