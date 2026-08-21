class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, s] for pos, s in zip(position, speed)]
        stack = []
        # reverse sorted order
        for pos, s in sorted(pair)[::-1]:
            # append the time taken 
            stack.append((target - pos) / s)
            # make sure atleast 2 cars are there to compare their times to destination
            # if the top of the stack one reaches the destination before the one thats ahead of it at index -2
            if len(stack) >=2 and stack [-1] <= stack[-2]:
                stack.pop()

        return len(stack)