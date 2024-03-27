class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals:
            if result[-1][1] >= interval[0]:
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
