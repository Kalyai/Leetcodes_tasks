class Solution(object):
    def generate(self, numRows):
        self.n = numRows
        trin = [1, 1]
        res = [[1, 1]] + [[]] * (numRows - 1)
        for j in range(1, numRows):
            for i in range(1, len(res[j - 1])):
                trin2 = res[j - 1][i - 1] + res[j - 1][i]
                trin = trin[:i] + [trin2] + trin[i:]
            if j > 1:
                for j1 in range(j - 1):
                    trin = trin[:-j + j1] + trin[-j + j1 + 1:]
            res[j] = trin
        res = [[1]] + res[:-1]
        return res
numRows = int(input())
print(Solution().generate(numRows + 1))