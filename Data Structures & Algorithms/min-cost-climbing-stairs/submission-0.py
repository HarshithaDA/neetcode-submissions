class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top of the staricase to reach 0
        # sove problem from right to left
        cost.append(0)

        # iterate thru reverse order
        # start from -3 so there are 2 values after that
        for i in range(len(cost)-3, -1, -1):
            # min cost of single and double jump
            cost[i] = min(cost[i]+ cost[i+1], cost[i]+ cost[i+2])

        return min(cost[0], cost[1])