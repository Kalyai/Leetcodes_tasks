class Solution(object):
    def partition(self, s):
        def make_palindroms(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for i in range(start, len(s)):
                if self.palindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    make_palindroms(i + 1, path)
                    path.pop()
        result = list()
        make_palindroms(0, [])
        return result


    def palindrome(self, s):
        return s == s[::-1]

res = Solution().partition('cdd')
print(res)