class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        zigzag = [[] for i in range(numRows)]
        row = 0
        flag = 0
        for i in range(len(s)):
            if row == numRows - 1:
                flag = 1
            elif row == 0:
                flag = 0

            zigzag[row] += s[i]

            if flag:
                row -= 1
            else:
                row += 1

        answer = ''
        for i in range(numRows):
            for z in zigzag[i]:
                answer += z
        return answer
        
