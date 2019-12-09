# encoding: utf-8
import asyncio

# async创建协程object , await调用就和正常顺序执行一样的效果
# 还可以通过create task 创建任务 , 事件循环+真正的并发
# 然后使用asyncio.run运行
# 一个非常好的编程规范是，asyncio.run(main()) 作为主程序的入口函数，在程序运行周期内，只调用一次 asyncio.run。

# await是同步调用
# 这段是用异步接口写了同步代码
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)

# % time
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

########## 输出 ##########

# crawling
# url_1
# OK
# url_1
# crawling
# url_2
# OK
# url_2
# crawling
# url_3
# OK
# url_3
# crawling
# url_4
# OK
# url_4
# Wall
# time: 10
# s
