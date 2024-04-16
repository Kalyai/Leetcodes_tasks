class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        origin_matrix = [row[:] for row in matrix]
        for j in range(n):
            fake_matrix = [row[:] for row in origin_matrix]
            for i in range(n - 1, -1, -1):
                fake_matrix[i][j], fake_matrix[j][i] = fake_matrix[j][i], fake_matrix[i][j]
            fake_matrix[j] = fake_matrix[j][::-1]
            matrix[j] = fake_matrix[j]
        return matrix
