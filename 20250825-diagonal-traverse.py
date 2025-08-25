# https://leetcode.com/problems/diagonal-traverse/
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        solution = []
        # O(mxn)
        index_i = 0
        index_j = 0
        while index_i < len(mat) and index_j < len(mat[0]) :
            if index_i > len(mat)-1 and index_j > len(mat[0])-1 :
                break 
            # Going up
            # i = i-1
            # j = j+1
            while index_i >= 0 and index_j < len(mat[0]) and index_i < len(mat) :
                solution.append(mat[index_i][index_j]) 
                index_i -= 1
                index_j += 1
            # Check if corner or side
            if index_j == len(mat[0]) :
                index_i += 2
                index_j -= 1
            elif index_i < 0 :
                index_i += 1
            # Going down
            # i = i+1
            # j = j-1
            while index_i < len(mat) and index_j >= 0 and index_j < len(mat[0]) :
                solution.append(mat[index_i][index_j]) 
                index_i += 1
                index_j -= 1
            # Check if corner or side
            if index_i == len(mat) :
                index_j += 2
                index_i -= 1
            elif index_j < 0 :
                index_j += 1
        return solution
        
