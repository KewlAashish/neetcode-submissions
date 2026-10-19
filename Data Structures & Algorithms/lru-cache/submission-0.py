class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.cache = {} #key -> Node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        return

    def insert(self, node):
        next = self.head.next
        node.next = next
        node.prev = self.head
        self.head.next = node
        next.prev = node

        return

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        val = node.val
        self.remove(node)
        self.insert(node)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        node = Node(key, value)
        self.cache[key] = node

        if len(self.cache.keys()) > self.k:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

        self.insert(node)

        return
        
