class Solution(object):
    def lengthOfLIS(self, nums):


        n = len(nums)
        res = [nums[0]]
        for i in range(1, n):
            if res[-1] > nums[i]:
                res[-1] = nums[i]
            elif res[-1] == nums[i]:
                continue
            else:
                if nums[i] > res[0]:
                    res.append(nums[i])
                else:
                    continue
            print(res)

        nums = res
        n = len(nums)
        res = [nums[0]]
        for i in range(1, n):
            if res[-1] > nums[i]:
                res[-1] = nums[i]
            elif res[-1] == nums[i]:
                continue
            else:
                if nums[i] > res[0]:
                    res.append(nums[i])
                else:
                    continue
            print(res)
        return len(res)
print(Solution().lengthOfLIS([0,1,0,3,2,3]))

