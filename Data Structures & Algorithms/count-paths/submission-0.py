class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom row is all 1s
        row = [1]*n

        # iterate thru all rows except last row
        for i in range(m-1):
            newrow = [1] * n
           # rightmost column all are going to be 1 (last value in every row)
           # start from second to last position and go in reverse r->l order
            for j in range(n-2, -1, -1):
                newrow[j] = newrow[j+1] + row[j]
            row = newrow

        return row[0]

