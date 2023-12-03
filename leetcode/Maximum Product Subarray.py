class Solution(object):
    def maxProduct(self, nums):
        mi, ma, res = nums[0], nums[0], nums[0]

        for i in range(len(nums)):
            x = ma
            ma = max({nums[i], ma * nums[i], mi * nums[i]})
            mi = min({nums[i], ma * nums[i], mi * nums[i]})
            res = max({nums[i], x * nums[i], mi * nums[i]})

        return res