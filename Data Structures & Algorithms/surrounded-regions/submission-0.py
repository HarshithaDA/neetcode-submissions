class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if regions are not connected to the border, flip it 
        # capture only the surrounded regions = capture everything except the unsurrounded regions (bordered regions)
        # mark the unsurrounded regions with a temp var
        # do a loop thru grid and anytime you see a 0 (part of surrounded regions) set it to x
        # do another loop thru grid and change the temp to os

        rows = len(board)
        cols = len(board[0])

        def capturedfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            capturedfs(r+1, c)
            capturedfs(r-1, c)
            capturedfs(r, c+1)
            capturedfs(r, c-1)

        # capture unsurrounded regions -> dfs -> o to temp
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O' and 
                    # check if its a border cell
                    (r in [0, rows-1] or c in [0, cols-1])):
                         capturedfs(r, c)

        # capture surrounded regions o->x
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O'):
                    board[r][c] = 'X'

        # uncapture unsurrounded regions -> temp back to o
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'T'):
                    board[r][c] = 'O'