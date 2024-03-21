class Solution(object):
    def twoSum(self, nums, target):
        cash = dict()
        for i in range(len(nums)):
            if target - nums[i] in cash:
                return [cash[target - nums[i]], i]
            
            if nums[i] not in cash:
                cash[nums[i]] = i
