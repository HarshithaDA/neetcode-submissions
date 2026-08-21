class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use max heap to get max value each time - log n operation
        # going to get max values n times so O(n log n)
        # python does not have max heap we have only min heap
        # to while using min heap we multiply all vslues with -1 and least will be least value at root so -8 example and u can take mod of this which will be the max value
        stones = [-s for s in stones] # min heap
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, first - second)
            
        return abs(stones[0]) if stones else 0