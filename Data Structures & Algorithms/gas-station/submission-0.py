class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)< sum(cost):
            return -1

        total=0
        start=0

        for i in range(len(gas)):
            total+=gas[i]-cost[i]

        # if total is ever negative we cannot go ahead with that position so set total back to 0 and move to next position to start

            if total<0:
                total=0
                start=i+1

        return start



