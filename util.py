import redis
import config
redis_client = redis.StrictRedis(host=config.redis_config['host'],
                                 port=config.redis_config['port'])


def get_book_info(key):
    if key.endswith('*'):
        keys = redis_client.keys(key)
        books = []
        for key in keys:
            info = redis_client.hgetall(key)
            books.append(info)
    else:
        books = redis_client.hgetall(key)
    return books
