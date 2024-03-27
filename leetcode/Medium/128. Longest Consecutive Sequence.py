class Solution(object):
    def longestConsecutive(self, nums):
        set_nums = set(nums)
        result = 0
      
        for elem in set_nums:
            if elem - 1 in set_nums:
                continue
              
            next = elem + 1
            cnt = 1
          
            while next in set_nums:
                next += 1
                cnt += 1
            result = max(result, cnt)
        return result
