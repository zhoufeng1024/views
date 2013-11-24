from util import redis_client


def douban_read(tree):
    books = tree.xpath('//div[@class="info"]')
    info = {}
    for book in books:
        info['title'] = book.xpath('.//div[@class="title"]/a/text()')[0]
        info['desc'] = book.xpath(
            './/div[@class="article-desc-brief"]/text()')[0]
        info['link'] = book.xpath('//div[@class="title"]/a/@href')[0]
        key = 'douban_read_%s' % info['title']
        redis_client.hmset(key, info)


def amazon_kindle(tree):
    info = {}
    books = tree.xpath('//div[@class="zg_title"]/a')
    for book in books:
        info['title'] = book.xpath('./text()')[0]
        info['link'] = book.xpath('./@href')[0].strip()
        key = 'amazon_kindle_%s' % info['title']
        redis_client.hmset(key, info)
