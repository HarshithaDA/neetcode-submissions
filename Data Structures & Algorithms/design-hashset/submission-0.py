class ListNode:
    def __init__(self, key):

        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        # hash function to get index
        index = key % len(self.set)
        # get head of linked list
        cur = self.set[index]

        # iterate through the end of that linked list to insert the node with same index hash
        while cur.next:
            # if you have duplicate nodes/value then skip it
            if cur.next.key == key:
                return 
            cur = cur.next
        
        # at last node insert the key
        cur.next = ListNode(key)


    def remove(self, key: int) -> None:
                # hash function to get index
        index = key % len(self.set)
        # get head of linked list
        cur = self.set[index]

                # iterate through the end of that linked list to insert the node with same index hash
        while cur.next:
            # if you have duplicate nodes/value then skip it
            # remove it
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next
        

    def contains(self, key: int) -> bool:
                        # hash function to get index
        index = key % len(self.set)
        # get head of linked list
        cur = self.set[index]

                # iterate through the end of that linked list to insert the node with same index hash
        while cur.next:
            # if you have duplicate nodes/value then skip it
            # if you found the value return true
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)