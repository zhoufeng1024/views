#-*-coding:utf-8-*-
jobs = [
    {'url': 'http://read.douban.com/ebooks/tag/计算机/?'
            'sort=new&cat=book',
     'callback': 'douban_read',
     },
    {'url': 'http://www.amazon.cn/gp/bestsellers/digital-text/143359071',
     'callback': 'amazon_kindle',
     }]


#max requests at the same time
max_clients = 10

#redis config
redis_config = {'host': '127.0.0.1', 'port': 6379}

# data update interval in seconds
interval = 120

server_port = 8888
