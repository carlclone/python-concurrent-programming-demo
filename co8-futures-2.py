import concurrent.futures
import requests
import threading
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # 主要区别 创建了线程池 , 然后让每个线程执行sites里的一条 (并发的)
    # 线程安全, 不会出现race condition是什么意思
    # 要配置合适的线程数 , 线程创建删除维护也有开销
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # with futures.ProcessPoolExecutor() as executor:  进程池 , 并行
        # future 的概念 : 参考评论里的回答, 类似期货 , 封存一个东西 , 平时不用去理会 , 在未来某个时候去看结果就行了
        # 我的理解 , 封装处于等待执行的操作 , 可以 用这个对象去查询状态 , JS里还可以给各个状态注册回调函数
        executor.map(download_one, sites)

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

## 输出
# Read 151021 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 129886 from https://en.wikipedia.org/wiki/Portal:Arts
# Read 107637 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 224118 from https://en.wikipedia.org/wiki/Portal:Society
# Read 184343 from https://en.wikipedia.org/wiki/Portal:History
# Read 167923 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 157811 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 91533 from https://en.wikipedia.org/wiki/Portal:Science
# Read 321352 from https://en.wikipedia.org/wiki/Computer_science
# Read 391905 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 180298 from https://en.wikipedia.org/wiki/Node.js
# Read 56765 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 468461 from https://en.wikipedia.org/wiki/PHP
# Read 321417 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 324039 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Download 15 sites in 0.19936635800002023 seconds