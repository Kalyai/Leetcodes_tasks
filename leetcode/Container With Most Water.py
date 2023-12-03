class Solution:
    def maxArea(self, height):
        ma = -1
        i = 0
        while i < len(height):
            f = height[i]
            for j in range(i+1, len(height)):
                ma = max(ma, (j - i) * min(f, height[j]))
            i += 1
        return ma

res = Solution().maxArea([1,8,6,2,5,4,8,3,6,5])
print(res)