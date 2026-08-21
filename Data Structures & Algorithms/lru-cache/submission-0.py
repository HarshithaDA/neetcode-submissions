class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmap key -> node
        # for most recent and least recent - dummy nodes
        # left = least recently used, right = most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        # initally we want to connect these nodes, and when putting a node in between we can 
        self.left.next, self.right.prev = self.right, self.left
    # remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


        # insert right before our right pointer
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        if key in self.cache:
            # remove and re insert it in right position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        # if key already in cache , there is already a node with same key value
        if key in self.cache:
            # remove node from our list
            self.remove(self.cache[key])
            # create new node with this key value pair and put in hashmap
        self.cache[key] = Node(key, value)
        # insert into list
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from list and detele the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]