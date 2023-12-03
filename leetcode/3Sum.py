class Solution(object):
    def threeSum(self, nums):
        l_n = len(nums)
        target = 0
        hash = dict()
        i = 0
        res = list()
        trash = list()
        while i < l_n:
            hash = dict()
            target = 0 + nums[i]
            for j in range(i + 1, l_n):
                if -(target + nums[j]) in hash and sorted([nums[i], nums[j], nums[hash[-(target + nums[j])]]]) not in res:
                    res.append(sorted([nums[i], nums[j], nums[hash[-(target + nums[j])]]]))
                    trash.append(i)
                    trash.append(j)
                    trash.append(hash[-(target + nums[j])])
                else:
                    hash[nums[j]] = j

            i += 1
        return res

res1 = Solution().threeSum([-1,0,1,2,-1,-4])
print(res1)#Вывод:  [[-1,-1,2],[-1,0,1]]

