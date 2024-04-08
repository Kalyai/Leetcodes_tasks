class Solution(object):
    def rob(self, nums):
        if len(nums) < 4:
            if nums: return max(nums)
            return nums

        dp1, dp2 = [0] * (len(nums) + 1), [0] * (len(nums) + 1)
        dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])
        dp2[2] = nums[1]

        for i1 in range(3, len(nums)):
            dp1[i1] = max(dp1[i1 - 2] + nums[i1 - 1], dp1[i1 - 1])

        for i2 in range(2, len(nums) + 1):
            dp2[i2] = max(dp2[i2 - 2] + nums[i2 - 1], dp2[i2 - 1])

        return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])