class Solution(object):
    def productExceptSelf(self, nums):
        zeroes = 0
        summ = 1
        result = [0] * len(nums)
        for num in nums:
            if num == 0:
                zeroes += 1
                continue
            summ *= num

        if zeroes == 1:
            for i in range(len(nums)):
                result[i] = summ if nums[i] == 0 else 0
            return result

        elif zeroes == 0:
            for i in range(len(nums)):
                result[i] = summ // nums[i]
            return result
        return result
