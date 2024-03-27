class Solution(object):
    def insert(self, intervals, newInterval):
        intervals = sorted(intervals, key=lambda x: x[0])
        len_intervals = len(intervals)
        i = 0
        result = list()

        while i < len_intervals:
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                result.append(interval)
            else: break
            i += 1

        while i < len_intervals:
            interval = intervals[i]
            if interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            else: break
            i += 1
        result.append(newInterval)

        while i < len_intervals:
            interval = intervals[i]
            result.append(interval)
            i += 1
        return result
