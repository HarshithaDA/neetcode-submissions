class MinStack:

    def __init__(self):
        # 2 stack
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        # take input value and append it to the stack
        self.stack.append(val)

        # for second staack append min till now
        # min of value and the value at the top of our stack- if stack is not empty
        # if stack is empty just the val and append it to minstack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # last value that was added
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
