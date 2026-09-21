class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op =="+":
                a,b = stack[-1], stack[-2]
                stack.append(a+b)

            elif op == "C":
                stack.pop()

            elif op == "D":
                prev = stack[-1]
                stack.append(prev*2)

            else:
                stack.append(int(op))

        return sum(stack)

