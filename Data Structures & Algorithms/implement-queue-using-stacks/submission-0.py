class MyQueue:
    # push to the back and pop from the front
    # use 2 stacks
    # pop from first stack 1 and push into stack 2 (reversed order)
    # push to stack 1 and pop from stack 2

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        # if stack 2 is empty remove eveything from stack 1 and push to stack 2 (you get the reversed order in stack 2)
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self) -> int:
        # if stack 2 is empty remove eveything from stack 1 and push to stack 2 (you get the reversed order in stack 2)
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # return element from front without poping it
        return self.stack2[-1]

        

    def empty(self) -> bool:
        return max(len(self.stack1), len(self.stack2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()