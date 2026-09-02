class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for each value in target triplet, check if and filter out the triplets that have values greater than the target values
        # if equal to target values, 
        # if all len(target)=3 values have been got, return true
        
        # positions we complete from target
        # return true if this equals len(target)=3
        good = set()

        # iterate input list
        for t in triplets:
            # greater than target values, filter out
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            # this triplet could contain values we are looking for
            # if value at position i is equal to target at i 
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3
            