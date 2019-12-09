# race condition ?

import requests
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    for site in sites:
        download_one(site)

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
# Read 184343 from https://en.wikipedia.org/wiki/Portal:History
# Read 224118 from https://en.wikipedia.org/wiki/Portal:Society
# Read 107637 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 151021 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 157811 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 167923 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 93347 from https://en.wikipedia.org/wiki/Portal:Science
# Read 321352 from https://en.wikipedia.org/wiki/Computer_science
# Read 391905 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 321417 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 468461 from https://en.wikipedia.org/wiki/PHP
# Read 180298 from https://en.wikipedia.org/wiki/Node.js
# Read 56765 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 324039 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Download 15 sites in 2.464231112999869 seconds