class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        firstRowZero = any(matrix[0][j] == 0 for j in range(n))
        firstColZero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
