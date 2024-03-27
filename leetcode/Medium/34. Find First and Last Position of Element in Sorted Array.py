class Solution(object):
    def searchRange(self, nums, target):
        def binary_search(nums, left, right, target):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return nums

        n = len(nums)
        middle = binary_search(nums, 0, n, target)
        left_index = middle
        while type(left_index) is int:
            left_index = binary_search(nums[:left_index], 0, left_index, target)
        left_index = len(left_index)


        right_index = middle
        while type(right_index) is int:
            nums = nums[right_index + 1:]
            right_index = binary_search(nums, 0, len(nums), target)
        right_index = n - len(nums) - 1
        
        if right_index == -1:
            return [-1, -1]
        return [left_index, right_index]
                
