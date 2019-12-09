import asyncio

# 引入了Task 任务的概念 , 有了任务 , 调度器就可以并发地执行多个任务 , 不会阻塞在某个任务
# 然后等待所有任务完成 , 完成时间约等于耗时最长的一个任务 , 因为大部分时间都消耗在sleep阻塞上,而不是cpu运行
# 只需要并发执行sleep , 然后等待多个中断 , 重新获得控制权         (想象成:某些负责执行sleep的计时器,通知cpu完成)

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

%time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

########## 输出 ##########

# crawling url_1
# crawling url_2
# crawling url_3
# crawling url_4
# OK url_1
# OK url_2
# OK url_3
# OK url_4
# Wall time: 3.99 s

