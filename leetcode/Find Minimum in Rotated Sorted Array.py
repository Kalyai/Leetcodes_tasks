class Solution(object):
    def findMin(self, nums):
        i, j = 0, len(nums) - 1
        while j > i:
            mid = (j + i) // 2
            

res = Solution().findMin([3,4,5,1,2])
print(res)