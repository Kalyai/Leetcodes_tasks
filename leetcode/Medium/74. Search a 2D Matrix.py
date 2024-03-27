class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[(mid // n)][(mid % n)]
            
            if target == num:
                return True
            
            elif num > target:
                right = mid - 1
                
            else:
                left = mid + 1
        return False
