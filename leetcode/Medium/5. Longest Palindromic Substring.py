class Solution(object):
    def longestPalindrome(self, s):
        def palindrom(left, right):
            while left >= 0 and right < len(s):
                if left - 1 >= 0 and s[left - 1] == s[right]:
                    left -= 1
                elif right + 1 < len(s) and s[left] == s[right + 1]:
                    right += 1
                else: break

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        result = s[0]
        for i in range(len(s)):
            string_palindrom = palindrom(i, i)
            if len(string_palindrom) > len(result):
                result = string_palindrom
        return result
