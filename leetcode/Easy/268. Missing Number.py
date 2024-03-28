class Solution(object):
    def missingNumber(self, nums):
        ma = 0
        set_nums = set()
        for i in range(len(nums)):
            if nums[i] > ma:
                ma = nums[i]
            set_nums.add(nums[i])
        
        for num in range(ma + 1):
            if num not in set_nums:
                return num
        return num + 1
        
