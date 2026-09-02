class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if overlap, merge
        # merge-> min(startindex of both), max(endindex of both)

        # if new interval's start index is greater than endindex of last interval -> add current interval to res

        # if new interval's end index is less than startindex of first interval -> add new interval to begining of original list

        res = []

        for i in range(len(intervals)):
            # not overlaping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # all intervals after it can be added to res
                return res + intervals[i:]

            # not overlapping
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # overlaping, so merge
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res