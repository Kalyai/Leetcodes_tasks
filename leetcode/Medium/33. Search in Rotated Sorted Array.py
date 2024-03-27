class Solution(object):
    def search(self, nums, target):
        if target == nums[0]:
            return 0

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                right = mid
            elif nums[mid] >= nums[0]:
                left = mid + 1

        if nums[0] > nums[right]:
            index_gap = right
            res = 0
            if nums[-1] < target:
                nums = nums[:index_gap]

            else:
                nums = nums[index_gap:]
                res += index_gap

            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res += mid
                    return res

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
