class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # tc O(1), sc O(n).
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_before_right(self, node):
        prev = self.right.prev

        prev.next = node
        node.next = self.right
        node.prev = prev
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value = self.cache[key].value
        # update, make this node mru
        self.remove(self.cache[key])
        self.insert_before_right(self.cache[key])

        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            # update, make this node mru
            self.remove(self.cache[key])
            self.insert_before_right(self.cache[key])
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert_before_right(self.cache[key])
            if self.capacity < len(self.cache):
                # evict lru
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]