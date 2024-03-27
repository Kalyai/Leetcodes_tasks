class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        res = 1
        left, right = 0, 1
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                res = max(right - left, res)
            else:
                left += 1
        
        return res
