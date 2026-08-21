class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            # if c is a closing parentheses -> cuz keys are parameters
            if c in closeToOpen:
                # stack is not empty and the last value we added in stack (top of stack) matches the opening parenthesis in the hashmap
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # open parentheses, then push it to the stack
                stack.append(c)

        return True if not stack else False