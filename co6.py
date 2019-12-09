import asyncio
import random

# 到这里就能知道 : 线程能实现的，协程都能做到
# 生产者消费者模型

# 协程和多线程的区别，主要在于两点，一是协程为单线程；二是协程由用户决定，在哪些地方交出控制权，切换到下一个任务。
# 协程的写法更加简洁清晰，把 async / await 语法和 create_task 结合来用，对于中小级别的并发需求已经毫无压力。
# 写协程程序的时候，你的脑海中要有清晰的事件循环概念，知道程序在什么时候需要暂停、等待 I/O，什么时候需要一并执行到底。

# 最后的最后，请一定不要轻易炫技。多线程模型也一定有其优点，一个真正牛逼的程序员，应该懂得，在什么时候用什么模型能达到工程上的最优，而不是自觉某个技术非常牛逼，所有项目创造条件也要上。技术是工程，而工程则是时间、资源、人力等纷繁复杂的事情的折衷。

# 思考题 : py的协程怎么实现回调函数?
# 使用asyncio获取事件循环，将执行的函数使用loop创建一个任务。add_done_callback将回掉函数传进去。
# 阻塞主要是同步编程中的概念:执行一个系统调用，如果暂时没有返回结果，这个调用就不会返回，那这个系统调用后面的应用代码也不会执行，整个应用被“阻塞”了。
async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)

async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))
        await asyncio.sleep(1)

async def main():
    queue = asyncio.Queue()

    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))

    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)

%time asyncio.run(main())

########## 输出 ##########

# producer_1 put a val: 5
# producer_2 put a val: 3
# consumer_1 get a val: 5
# consumer_2 get a val: 3
# producer_1 put a val: 1
# producer_2 put a val: 3
# consumer_2 get a val: 1
# consumer_1 get a val: 3
# producer_1 put a val: 6
# producer_2 put a val: 10
# consumer_1 get a val: 6
# consumer_2 get a val: 10
# producer_1 put a val: 4
# producer_2 put a val: 5
# consumer_2 get a val: 4
# consumer_1 get a val: 5
# producer_1 put a val: 2
# producer_2 put a val: 8
# consumer_1 get a val: 2
# consumer_2 get a val: 8
# Wall time: 10 s