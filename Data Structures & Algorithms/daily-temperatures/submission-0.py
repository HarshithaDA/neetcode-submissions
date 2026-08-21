class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = [] # pair : [temp, index]

        for i, t in enumerate(temperatures):
            # is our stack not empty and is the temp greater than the value at the top of our stack
            while stack and t>stack[-1][0]:
                # stack[-1][0] -1 cuz we want the top of stack value and 0 cuz temperature is first value in that t,i pair
                stackT, stackInd = stack.pop()
                # number of days it took to find a grater temperature and then just append that at the corresponding position
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res
