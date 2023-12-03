class Solution(object):
    def containsDuplicate(self, nums):
        cash = dict()
        for i, num in enumerate(nums):
            if num in cash:
                return True
            cash[num] = i
        else:
            return False
