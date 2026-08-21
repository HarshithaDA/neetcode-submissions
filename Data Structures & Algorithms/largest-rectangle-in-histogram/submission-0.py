class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair - index, height

        for i, h in enumerate(heights):
            # start index of this bar is at i
            # we do not know just yet if it can be extended back or front
            startIndex = i
            # while stack is not empty and 
            # while top value in stack and the top values height is greater than the height ewe just reached
            while stack and stack[-1][1] > h:
                # pop the height
                index, height = stack.pop()
                # check max rectangle we can create from that height
                maxArea = max(maxArea, height*(i-index))
                # extend the current height we are at backwards to the index we just poped
                startIndex = index
            # add the pair
            stack.append((startIndex, h))


            # other entries that extend till the end of the histogram
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea

