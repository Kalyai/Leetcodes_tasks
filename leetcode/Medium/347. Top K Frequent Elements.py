class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cash = dict()
        for n in nums:
            if n not in cash:
                cash[n] = 0
            cash[n] += 1

        return sorted(cash, key=lambda x: cash[x], reverse=True)[:k]
        #Solution 0(t*log(t)), t = uniq_elem(nums)
