class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = 1

        # Step 1: Mark rows and columns
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Set zeroes
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: First row
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: First column
        if col0 == 0:
            for i in range(rows):
                matrix[i][0] = 0
