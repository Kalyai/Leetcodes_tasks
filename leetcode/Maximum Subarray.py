class Solution(object):
    def maxSubArray(self, nums):
        l_n = len(nums)
        pr = [0] * (l_n + 1)
        for i in range(l_n):
            pr[i+1] = pr[i] + nums[i]

        ma = pr[-1]
        for i in range(l_n+1):
            for j in range(i+1, l_n+1):
                ma = max(ma, pr[j] - pr[i])


        for i in range(l_n):
            x = nums[i]

            if pr[i+1] > ma: ma = pr[i+1]

        return ma
