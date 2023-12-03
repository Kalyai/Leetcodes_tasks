import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        arr = [nums.pop(0)]

        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                l, r = 0, len(arr) - 1
                m = (l + r) // 2


res = Solution().lengthOfLIS([1,8,4,5,3,7])
print(res)