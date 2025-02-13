class NestedIterator:
    # tc O(n+l), sc O(n+l).
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque()
        self.flattenlist(nestedList)
    
    def flattenlist(self, l):
        for item in l:
            if item.isInteger():
                self.queue.append(item.getInteger())
            else:
                self.flattenlist(item.getList())
    
    def next(self) -> int:
        return self.queue.popleft()
        
    def hasNext(self) -> bool:
        return len(self.queue) > 0