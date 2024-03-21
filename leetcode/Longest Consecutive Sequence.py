class Solution(object):
    def longestConsecutive(self, nums):
        set_nums = set(nums)

        res = 0
        for s in set_nums:
            if s - 1 in set_nums:
                continue
            end = s + 1
            cnt = 1
            while end in set_nums:
                end += 1
                cnt += 1
            res = max(res, cnt)
        return res
