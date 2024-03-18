class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        dynamic_str = dict()
        res = 0

        for right in range(len(s)):
            if s[right] not in dynamic_str:
                dynamic_str[s[right]] = 0
            dynamic_str[s[right]] += 1

            check = right - left + 1
            if check - max(dynamic_str.values()) <= k:
                res = max(res, check)

            else:
                dynamic_str[s[left]] -= 1
                left += 1
                if dynamic_str[s[left]] == 0:
                    dynamic_str.pop(s[left])
        return res

