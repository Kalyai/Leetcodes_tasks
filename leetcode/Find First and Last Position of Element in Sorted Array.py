#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
class Solution():
    def searchRange(self, nums, target):
        self.nums = nums
        self.target = target
        res = []
        dlina = len(nums)
        if dlina > 1:
            l1 = -1

            r1 = -1
            i = 0

            while i != dlina//2+1:

                if l1 == target:
                    res.append(i - 1)
                    while l1 == nums[i]:
                        l1 = nums[i]
                        if i + 1 == dlina:
                            i += 1
                            break
                        else:
                            i += 1
                    res.append(i - 1)
                    break
                else:
                    l1 = nums[i]

                if r1 == target:
                    index = dlina - i
                    while r1 == nums[-i-1]:
                        r1 = nums[-i-1]
                        i += 1
                    res.append(dlina - i)
                    res.append(index)
                    break
                else:
                    r1 = nums[-i-1]
                i += 1
            if l1 == target and res == []:
                res = [i-1, i-1]

        elif dlina == 1 and target == nums[0]:
            res = [0, 0]

        if len(res) != 2:
            res = [-1, -1]
        return res

attempt = Solution().searchRange([2, 2], 2)
print(attempt)