class Solution(object):
    def convert(self, s, numRows):
        self.s = s
        self.numRows = numRows
        fin = [ [] for i in range(numRows)]
        if numRows != 1:
            i = 0
            row = 0
            fl = 0
            while i < len(s):
                fin[row] += s[i]
                i += 1
                if not(fl):
                    row += 1
                else:
                    row -= 1

                if row == 0:
                    fl = 0
                elif row == numRows - 1:
                    fl = 1
            res = str()
            for row1 in fin:
                for row2 in row1:
                    res += row2
            return res
        else:
            return s

#res = Solution().convert('PAYPALISHIRING', 3)
res = Solution().convert('AB', 1)
print(res) #"PAHNAPLSIIGYIR"