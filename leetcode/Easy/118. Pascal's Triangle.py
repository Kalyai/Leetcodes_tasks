class Solution(object):
    def generate(self, numRows):
        row = [1, 1]
        res = [[1, 1]] + [[]] * (numRows - 1)
        for j in range(1, numRows):
            for i in range(1, len(res[j - 1])):
                part_row = res[j - 1][i - 1] + res[j - 1][i]
                row = row[:i] + [part_row] + row[i:]
            
            if j > 1:
                for j1 in range(j - 1):
                    row = row[:-j + j1] + row[-j + j1 + 1:]
                
            res[j] = row
        res = [[1]] + res[:-1]
        return res
