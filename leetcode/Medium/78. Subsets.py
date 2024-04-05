class Solution(object):
    def subsets(self, nums):
        def backtrack(subset, i):
            if i == len(nums):
                res.append(subset[::])
                return
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()
            backtrack(subset, i + 1)

        res = list()
        backtrack([], 0)
        return res
