class TimeMap(object):
    def __init__(self):
        self.data = {}
        self.time = {}

    def set(self, key, value, timestamp):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(value)

        if key not in self.time:
            self.time[key] = []
        self.time[key].append(timestamp)

    def get(self, key, timestamp):
        if str(key) not in self.time:
            return ''

        timeline = self.time[key]
        index = self.binary_search(timeline, timestamp)

        if key in self.data and index != -1:
            return self.data[key][index]
        return ''

    def binary_search(self, timeline, target):
        left, right = 0, len(timeline) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if timeline[mid] == target:
                return mid
            
            elif timeline[mid] < target:
                left = mid
                
            else:
                right = mid - 1

        if timeline[left] <= target:
            return left
        return -1
