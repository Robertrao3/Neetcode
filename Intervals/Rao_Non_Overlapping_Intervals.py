class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()

        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = min(lastEnd, end)
        return res