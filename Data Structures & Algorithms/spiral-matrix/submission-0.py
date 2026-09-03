class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # outer layer first
        # go layer by layer l-=1, r-=1 inward and top+=1, b-=1
        # once r is reached, top incremented by 1, right by  and do the same l->r

        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        output = []

        while left<right and top<bottom:
            # left->right
            for i in range(left, right):
                output.append(matrix[top][i])
            # shift top down after 1 layer
            top+=1

            # get every i in right col
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            # shift right to left after 1 layer
            right-=1

            if not(left<right and top<bottom):
                break

            # bottom row right->left backwards
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            # shift bottom by one layer up
            bottom -=1

            # get every i in left col
            for i in range(bottom -1,top-1, -1):
                output.append(matrix[i][left])
            # shift left to right by 1
            left+=1

        return output



