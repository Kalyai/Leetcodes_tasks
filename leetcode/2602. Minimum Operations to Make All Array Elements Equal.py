class Solution:
    def minOperations(self, nums, queries):
        n = len(nums)
        m = len(queries)
        nums.sort()
      
        for i in range(m):
            queries[i] = [queries[i], i]
        queries.sort()
      
        res = [0] * m
        i = 0
        su = 0
        rsum = sum(nums)
        for m, pos in queries:
            while i < n and nums[i] <= m:
                su += nums[i]
                rsum -= nums[i]
                i += 1
            res[pos] = i * m - su + rsum - m * (n - i)
        return res
