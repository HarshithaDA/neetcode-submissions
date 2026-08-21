class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
           # using minheap

        minHeap = []
        for x,y in points:
            # find distance
            dist = (x **2) + (y ** 2)
            # dist is the key
            minHeap.append([dist, x,y])

        heapq.heapify(minHeap)
        res = []
        while k>0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1

        return res