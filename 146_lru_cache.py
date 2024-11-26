class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as recently used
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old key so it can be reinserted at the end
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove the first key (the least recently used one)
            oldest_key = next(iter(self.cache))
            self.cache.pop(oldest_key)
        # Insert the new key-value pair
        self.cache[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
