#-*-coding:utf-8
import config
import pipeline
import util
from lxml import etree
from collections import deque
from tornado.gen import coroutine
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler, Application


queue = deque()
http = AsyncHTTPClient(max_clients=config.max_clients)


class MainHandler(RequestHandler):
    def get(self, source):
        if source == 'douban':
            self.render('views/list.html',
                        books=util.get_book_info('douban_read*'))
        elif source == 'amazon':
            self.render(
                'views/list.html', books=util.get_book_info('amazon_kindle*'))


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
    PeriodicCallback(main, config.interval * 1000).start()


@coroutine
def process(job):
    response = yield http.fetch(job['url'])
    tree = etree.HTML(response.body.decode('utf-8'))
    getattr(pipeline, job['callback'])(tree)


if __name__ == '__main__':
    io_loop = IOLoop.instance()
    io_loop.add_callback(main)
    application = Application([
        (r'/(.*)', MainHandler)])
    application.listen(config.server_port)
    io_loop.start()
