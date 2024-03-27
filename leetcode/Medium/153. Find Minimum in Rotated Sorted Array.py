class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                right = mid
            
            elif nums[mid] >= nums[0]:
                left = mid + 1

        return min(nums[right], nums[0])
