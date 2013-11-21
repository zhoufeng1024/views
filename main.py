#-*-coding:utf-8
import config
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from collections import deque
from lxml import etree

queue = deque()
http = AsyncHTTPClient(max_clients=config.max_clients)


def main():
    for entry in config.jobs:
        queue.append(entry)
    while True:
        try:
            job = queue.pop()
        except IndexError:
            break
        else:
            process(job)
    #how?never?stop when process finished
    #IOLoop.instance().stop()


@coroutine
def process(job):
    response = yield http.fetch(job['url'])
    tree = etree.HTML(response.body)
    print tree.xpath('//article').__dict__


def test():
    main()


if __name__ == '__main__':
    io_loop = IOLoop.instance()
    io_loop.add_callback(main)
    io_loop.start()
