
class Solution(object):
    def productExceptSelf(self, nums):
        l_nums = len(nums)
        if 0 not in nums:
            pr = [1] * (l_nums + 1)
            for i in range(l_nums):
                pr[i+1] = pr[i] * nums[i]
            sm_nums = pr[-1]

            res = list()
            for i in range(l_nums):
                x = nums[i]
                res.append(sm_nums // x)

            return res
        else:
            res = list()
            cnt_0 = 0
            index_0 = 0
            pr = [1] * (l_nums + 1)
            for i in range(l_nums):
                if nums[i] == 0:
                    cnt_0 += 1
                    index_0 = i
                    pr[i+1] = pr[i]
                else: pr[i+1] = pr[i] * nums[i]
            if cnt_0 == 1:
                for i in range(l_nums):
                    x = nums[i]
                    if x == 0:
                        res.append(pr[-1])
                    else: res.append(0)
            else: res = [0] * l_nums
            return res


res = Solution().productExceptSelf([1,2,3,4])
print(res)