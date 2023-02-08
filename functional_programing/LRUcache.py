from collections import OrderedDict


class LRUcache():
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.pop(key)  # 把陈旧的缓存删除
            self.cache[key] = value  # 更新缓存
            print(value)
            return value
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)  # 把陈旧的缓存删除
            self.cache[key] = value
        elif len(self.cache) >= self.size:
            # 没有命中缓存，并且缓存容量已满
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value


if __name__ == '__main__':
    cache = LRUcache(3)
    cache.set(1, 2)
    cache.set(2, 3)
    cache.set(3, 4)
    cache.set(4, 5)
    cache.set(5, 6)
    cache.set(6, 7)
    cache.get(5)
