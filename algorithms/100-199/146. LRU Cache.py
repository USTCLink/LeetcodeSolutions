class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            val = self.dic[key]
            del self.dic[key]
            self.dic[key] = val
            return val      

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            if len(self.dic) >=  self.capacity:
                self.dic.popitem(last = False)
            self.dic[key] = value
        else:
            del self.dic[key]
            self.dic[key] = value