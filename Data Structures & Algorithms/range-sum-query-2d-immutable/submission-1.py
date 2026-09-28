class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # building matrix with rows and columns
        self.summat = [[0]* (cols +1) for r in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                # sum of the rectangle above
                rectangleAbove = self.summat[r][c+1]
                # sum of current rectangle is prefix + sum of rectangle above
                self.summat[r+1][c+1] = prefix+ rectangleAbove

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # r1,c1 -> top left
        # r2, c2 -> bottom right
        r1, c1 = row1+1, col1+1
        r2, c2 = row2+1, col2+1

        # area of rectangle
        bottomright = self.summat[r2][c2]
        abovearea = self.summat[r1-1][c2]
        left = self.summat[r2][c1-1]
        topleft = self.summat[r1-1][c1-1]

        return bottomright - abovearea - left + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)