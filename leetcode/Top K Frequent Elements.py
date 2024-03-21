class Solution(object):
    def topKFrequent(self, nums, k):
        cash = dict()
        for n in nums:
            if n not in cash:
                cash[n] = 0
            cash[n] += 1

        return sorted(cash, key=lambda x: cash[x], reverse=True)[:k]
