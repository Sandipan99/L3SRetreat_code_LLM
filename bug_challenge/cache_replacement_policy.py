class Cache:
    def __init__(self, cache_size):
        self.cache = [None] * cache_size
        self.rrpv = [3] * cache_size

    def access(self, data):
        if data in self.cache:
            self.rrpv[self.cache.index(data)] = 0
        else:
            if 3 in self.rrpv:
                index = self.rrpv.index(3)
                self.cache[index] = data
                self.rrpv[index] = 2
            else:
                for i in range(len(self.rrpv)):
                    self.rrpv[i] += 1

    def print_cache(self):
        print(self.cache)

cache = Cache(3)
cache.access('a')
cache.access('b')
cache.access('c')
cache.access('a')
cache.access('d')
cache.print_cache()
