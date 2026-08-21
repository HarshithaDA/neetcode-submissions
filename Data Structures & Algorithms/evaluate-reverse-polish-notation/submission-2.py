class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            # pop from our stack twice and do the operation with those two values together
            # then append that result
           if c == "+":
                stack.append(stack.pop() + stack.pop())
           elif c == "-":
                a, b = stack.pop(), stack.pop()
            # take the one that was poped second and subtract it from the one that was poped first
                stack.append(b-a)
           elif c == "*":
                stack.append(stack.pop() * stack.pop())
           elif c == "/":
                # in qn we have to round it towards 0 so in python we call the int function that will convert it to an integer and round it at the same time
                a, b = stack.pop(), stack.pop()
                # take the one that was poped second and divide it from the one that was poped first
                stack.append(int(b/a))
           else:
                # number
                # convert character to number and append it to the stack
                stack.append(int(c))

        return stack[0]