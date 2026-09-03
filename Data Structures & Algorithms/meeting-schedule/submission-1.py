"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        # if overlapping - return false
        # if non overlaping - return true

        # sort based on start times
        intervals.sort(key= lambda i: i.start)

        # compare start time of second interval & end time of first interval - if before return false else true

        prevend = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < prevend:
                return False
            prevend = interval.end

        return True

