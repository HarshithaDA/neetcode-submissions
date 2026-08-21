class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # two pointers - one for top row and one for bottom row
        top, bot = 0, ROWS-1

        while top<=bot:
            # applying binary search
            middlerow = (top+bot)//2
            # look at the largest value in this row (last value of the row)
            # see if its less than target value
            # rightmost value so -1
            # is target value greater than the largest value in this row
            if target>matrix[middlerow][-1]:
                # if yes, look at the next row down - for larger values
                top = middlerow+1
            # target value smaller than the largest value in this row
            elif target<matrix[middlerow][0]:
                # move up one row
                bot =middlerow-1
            else:
                # target is in this current row
                break

        # if none of the rows have the target value it exits the while loop
        if not (top<=bot):
            return False
        
        # current row has the target value
        # run binary search on this row
        middlerow = (top+bot)//2
        # setting 2 pointers
        l,r = 0, COLS-1

        while l<=r:
            # middle value
            m = (l+r)//2
            if target>matrix[middlerow][m]:
                # search towards the right of this row
                    l = m+1
                # search towards the left of this row
            elif target<matrix[middlerow][m]:
                    r = m-1
                # target is the middle value of the row - already reached
            else:
                return True
        # never found the target value
        return False




