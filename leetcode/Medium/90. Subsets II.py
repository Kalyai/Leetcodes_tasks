class Solution(object):
    def subsetsWithDup(self, nums):
        def backtrack(subset, i):
            if i == len(nums):
                res.append([i for i in subset])
                return

            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(subset, i + 1)

        res = []
        nums.sort()
        backtrack([], 0)
        return res
