class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # finding smallest of 2 intervals - the one that has min length

        # sort intervals by start
        intervals.sort()

        # add all possible intervals that this query q could belong to to the minheap
        # IF START of an interval IS > Q then does not belong
        # IF START/END is = Q then belongs
        # iterate till start is <= Q then belongs
        # if belongs, add length to minheap, also add end value
        # if 2 have same length, pop the one that has less end value first
        # add the smallest len to output
        # another hashmap to keep order of queries and output

        minheap = [] # len, endvalue/rightvalue of interval

        res = {}
        i = 0
        # start = intervals[i][0]
        # end = intervals[i][1]

        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                # push len and end value to minheap
                heapq.heappush(minheap, (r-l+1, r))
                i+=1

            # pop from minheap - if interval that q does not belong to
            # smallest interval's right value < q - pop
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            # if there are intervals in minheap and append the length
            res[q] = minheap[0][0] if minheap else -1

        return [res[q] for q in queries]




