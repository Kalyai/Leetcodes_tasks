class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        l, r = 0, 0
        ma = 0
        while r + 1 < len(s):
            if s[r + 1] not in s[l:r + 1]:
                r += 1
            else:
                l += 1
                if l >= r:
                    r = l
            ma = max(ma, r - l + 1)
        return ma