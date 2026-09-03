"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # goal: to find max no. of overlapping meetings

        # count: no. of active meetings at the moment

        # decrement count if end has reached in one interval
        # increment count if start has reached in one interval
        # check max count has ever reached and return it

        # if 2 points have same value, always iterate thru end meeting time first before start meeting time and pick one that ends first - (non overlapping)


        # start times and end times in separate sorted arrays
        # 2 pointers for each array
        # pick min of both and compare
        # if min between both is start time - increment count & shift start ptr by 1
        # if both are equal - visit end time first - decrement count by 1 - shift end ptr by 1
        # if min between both is end time - 


        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0 # no. of active mettings currently
        res = 0 # max of count ever reached

        s,e = 0,0 # pointers

        if not intervals:
            return 0 

        # s is always going to reach the end of intervals before e does
        while s<len(intervals):
            # 
            if start[s] < end[e]:
                count+=1
                s+=1
            # 
            # start[s] == end[e]:
            else:
                count-=1
                e+=1
            
            res=max(count, res)

        return res


