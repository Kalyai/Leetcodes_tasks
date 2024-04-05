class Solution(object):
    def permute(self, nums):
        result = list()
        if len(nums) == 1:
            return [[i for i in nums]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
