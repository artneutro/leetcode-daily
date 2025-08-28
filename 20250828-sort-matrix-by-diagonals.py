# https://leetcode.com/problems/sort-matrix-by-diagonals/
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # O(n) + O(nlogn) + O(n)
        index_i = len(grid)-1
        index_j = 0
        descend = True
        counter = 1
        while counter > 0 :
            internal_i = index_i
            internal_j = index_j
            # Get next diagonal
            current_diag = []
            while internal_i < len(grid) and internal_j < len(grid) :
                current_diag.append(grid[internal_i][internal_j])
                internal_i += 1
                internal_j += 1
            # Sort diagonal
            if descend :
                current_diag = sorted(current_diag, reverse=True)
            else :
                current_diag = sorted(current_diag)
            # Write sorted diagonal
            internal_i = index_i
            internal_j = index_j
            diag_index = 0
            while internal_i < len(grid) and internal_j < len(grid) :
                grid[internal_i][internal_j] = current_diag[diag_index]
                internal_i += 1
                internal_j += 1
                diag_index += 1
            # Check if arrived to main diag
            if len(current_diag) == len(grid) :
                descend = False
            # Reset values for next diagonal
            if descend :
                index_i -= 1
                index_j = 0
                counter += 1
            else :
                index_i = 0
                index_j += 1
                counter -= 1
        return grid
