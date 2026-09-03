class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotate outermost layer first in reverse order so we only need 1 temp variable while replacing values
        # stop when l>R
        # for next layer, shift top left by 1pos right, top right by 1pos down, bottom right by 1pos left, bottom left by 1pos up -> do these with i

        l,r = 0, len(matrix) - 1

        while l<r:
            # top row - except last element
            for i in range(r-l):
                top, bottom = l,r

                # save topleft value
                temp = matrix[top][l + i]

                # move bottom left to top left's position
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left to top right 
                # we overwrote the top left but its fine since its saved in temp
                matrix[top + i][r] = temp

            r-=1
            l+=1

