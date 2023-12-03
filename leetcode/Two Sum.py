class Solution(object):
    def twoSum(self, nums, target):
        len_nums = len(nums)
        serch = dict()

        for i in range(len_nums):
            x = nums[i]

            if (target - x) in serch and serch is not None:
                return [serch[target - x], i]
            serch[x] = i

res = Solution().twoSum([3, 3], 6)
print(res)