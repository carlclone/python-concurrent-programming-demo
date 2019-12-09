import concurrent.futures
import requests
import time

# 解释器不是线程安全的 , py有 GIL , 同一时刻
# 线程安全是什么 https://en.wikipedia.org/wiki/Thread_safety
#  下面的一条评论: Future 是一个任务队列模型，所有需要IO的任务，都进入队列，然后根据IO和CPU的使用来回调度任务，合理配置IO和CPU的资源。 可以结合js的事件循环模型一起理解
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)

        # 有完成的就执行 , 避免阻塞在某个future上 , 类似事件循环吧
        for future in concurrent.futures.as_completed(to_do):
            future.result()
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()

# 输出
# Read 129886 from https://en.wikipedia.org/wiki/Portal:Arts
# Read 107634 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 224118 from https://en.wikipedia.org/wiki/Portal:Society
# Read 158984 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 184343 from https://en.wikipedia.org/wiki/Portal:History
# Read 157949 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 167923 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 94228 from https://en.wikipedia.org/wiki/Portal:Science
# Read 391905 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 321352 from https://en.wikipedia.org/wiki/Computer_science
# Read 180298 from https://en.wikipedia.org/wiki/Node.js
# Read 321417 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 468421 from https://en.wikipedia.org/wiki/PHP
# Read 56765 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 324039 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Download 15 sites in 0.21698231499976828 seconds