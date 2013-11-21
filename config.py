jobs = [
    {'url': 'http://read.douban.com/ebooks/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA/?'
            'sort=new&cat=book',
     'callback': 'douban_read_top',
     },
    {'url': 'http://www.amazon.cn/gp/bestsellers/digital-text/143359071',
     'callback': 'amazon_kindle_top',
     }]


max_clients = 10
