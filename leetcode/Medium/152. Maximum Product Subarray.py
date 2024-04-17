class Solution(object):
    def maxProduct(self, nums):
        min_result = max_result = result = nums[0]

        for num in nums[1:]:
            min_now = min_result * num
            max_now = max_result * num

            min_result = min(max_now, min_now, num)
            max_result = max(min_now, max_now, num)

            result = max(result, max_result)

        return result