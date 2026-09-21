class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        # loop while we havent reached last element
        for i in range(len(self.q) -1):
            # pop from left (except last element) & add it to the right most side
            self.push(self.q.popleft()) 
        # return the last element 
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        if not self.q:
            return True
        else:
            return False        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()