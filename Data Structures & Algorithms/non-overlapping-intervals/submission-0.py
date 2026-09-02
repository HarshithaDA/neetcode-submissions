class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # is two intervals have same edge point (start index of interval 1 and endindex of interval 2 are equal) and if start is greater than end -> nonoverlaping

        # sort by starting point & compare adjancent pairs
        # if interval 2 starts before the interval 1 ends, -> overlapping
        # if interval 2 starts before the interval 1 and interval 2 ends after interval 1 ends -> overlapping

        # which one to remove? -> pick the one that ends last (one with larget endvalue)

        intervals.sort()

        # count to remove
        res = 0

        # keep track of 1st end value
        prevend = intervals[0][1]

        # iterate thru remaining intervals
        for start, end in intervals[1:]:
            # non overlaping
            if start >= prevend:
                # update new end value
                prevend = end

            # overlaping
            else:
                # remove one interval
                res +=1
                # keep the one that has the min end value
                prevend = min(end, prevend)

        return res



