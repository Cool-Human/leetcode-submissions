class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = []

    def get(self, key: int) -> int:
        for i in range(len(self.store)):
            if self.store[i][0] == key:
                self.store.insert(0, self.store.pop(i))
                return self.store[0][1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.store)):
            if self.store[i][0] == key:
                temp = self.store.pop(i)
                temp[1] = value
                self.store.insert(0, temp)
                return
        if len(self.store) == self.capacity:
            self.store.pop()
        self.store.insert(0, [key, value])
        return
