class Solution:
    def minOperations(self, nums, queries):
        n = len(nums)
        q = len(queries)
        nums.sort()
        for i in range(q):
            queries[i] = [queries[i], i]
        queries.sort()
        res = [0] * q
        i = 0
        s = 0
        rsum = sum(nums)
        for q, pos in queries:
            while i < n and nums[i] <= q:
                s += nums[i]
                rsum -= nums[i]
                i += 1
            res[pos] = i * q - s + rsum - q * (n - i)
        return res