class Solution(object):
    def characterReplacement(self, s, k):
        cash = dict()
        left = 0
        result = 1
      
        for right in range(len(s)):
            if s[right] not in cash:
                cash[s[right]] = 0
            cash[s[right]] += 1

            replacement = right - left + 1
            if replacement - max(cash.values()) <= k:
                result = max(result, replacement)

            else:
                cash[s[left]] -= 1
                if cash[s[left]] == 0:
                    cash.pop(s[left])
                left += 1
        return result
