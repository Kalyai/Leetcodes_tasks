class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        def backtracking(number, cur_s):
            if len(cur_s) == len(digits):
                result.append(cur_s)
                return
            for i in range(len(cheme[digits[number]])):
                now = cheme[digits[number]][i]
                backtracking(number + 1, cur_s + now)

        cheme = {"2": "abc",
                 "3": "def",
                 "4": "ghi",
                 "5": "jkl",
                 "6": "mno",
                 "7": "pqrs",
                 "8": "tuv",
                 "9": "wxyz"
                }

        result = list()
        backtracking(0, '')
        return result
