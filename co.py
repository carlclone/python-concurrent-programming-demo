# encoding: utf-8
import time


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    # 阻塞 , cpu有大量闲置时间 , 可以使用并发编程优化
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)

# % time
main(['url_1', 'url_2', 'url_3', 'url_4'])


#
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