# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Iterate over the matrix to look for zeroes - O(n*m)
        index_row = 0
        index_col = 0
        while index_row < len(matrix) :
            while index_col < len(matrix[0]) :
                # If a zero is found, do the transformations (skip other zeroes) - O(n+m)
                if matrix[index_row][index_col] == 0 :
                    # Process all rows
                    internal_row = 0
                    while internal_row < len(matrix) :
                        if matrix[internal_row][index_col] != 0 :
                            matrix[internal_row][index_col] = None
                        internal_row += 1
                    # Process all cols
                    internal_col = 0
                    while internal_col < len(matrix[0]) :
                        if matrix[index_row][internal_col] != 0 :
                            matrix[index_row][internal_col] = None
                        internal_col += 1
                index_col += 1
            index_row += 1
            index_col = 0
        # Iterate over the matrix to look for NULL and convert to zeroes - O(n*m)
        index_row = 0
        index_col = 0
        while index_row < len(matrix) :
            while index_col < len(matrix[0]) :
                if matrix[index_row][index_col] == None :
                    matrix[index_row][index_col] = 0
                index_col += 1
            index_row += 1
            index_col = 0
        #return matrix
        
