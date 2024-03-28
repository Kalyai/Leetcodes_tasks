class Solution(object):
    def containsDuplicate(self, nums):
        cash = set()
        for n in nums:
            if n in cash:
                return True
            cash.add(n)
        return False
        
