class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        # recursive call for all values from nums without the first element
        perms = self.permute(nums[1:])
        # add number at index 0 to all these perms to get combinations
        res = []

        for p in perms:
            # go through every possible index position for each permutation to insert
            # we can go till right of number to insert so p+1
            for i in range(len(p)+1):
                p_copy=p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)


        return res