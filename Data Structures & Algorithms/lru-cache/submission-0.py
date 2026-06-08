class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_map = {}
        
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = Node(key,value)
        self.insert(self.hash_map[key])

        if len(self.hash_map) > self.cap:
            lr = self.left.next
            self.remove(lr)
            del self.hash_map[lr.key]
        