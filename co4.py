import asyncio


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)     # 任务调度点 , cpu闲置 , 调度到其他任务执行
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)    # 任务调度点 , cpu闲置 , 调度到其他任务执行
    print('worker_2 done')


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2()) # 实际上创建完后就开始调度了
    print('before await')
    await task1      #同步的 , 等待task1完成后执行
    print('awaited worker_1')
    await task2  #同上
    print('awaited worker_2')

% time
asyncio.run(main()) #启动调度

########## 输出 ##########

# before await
# worker_1 start
# worker_2 start
# worker_1 done
# awaited worker_1
# worker_2 done
# awaited worker_2
# Wall time: 2.01 s