class Solution(object):
    def productExceptSelf(self, nums):
        cnt_0 = 0
        for n in nums:
            if n == 0:
                cnt_0 += 1
    
        if cnt_0 > 1:
            return [0] * len(nums)
    
        elif cnt_0 == 1:
            su = 1
            index_0 = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    su *= nums[i]
                else:
                    index_0 = i
    
            res = [0] * len(nums)
            res[index_0] = su
            return res
    
        else:
            su = 1
            for i in range(len(nums)):
                su *= nums[i]
    
            res = list()
            for i in range(len(nums)):
                res.append(su//nums[i])
            return res
