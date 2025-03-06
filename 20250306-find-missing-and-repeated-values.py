# https://leetcode.com/problems/find-missing-and-repeated-values/
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        solution = [-1, -1]
        n = len(grid)**2
        storage = n*[-1]
        index_i = 0
        index_j = 0
        while index_i < len(grid) :
            while index_j < len(grid[0]) :
                if storage[grid[index_i][index_j]-1] == -1  :
                    storage[grid[index_i][index_j]-1] = 1
                else :
                    solution[0] = grid[index_i][index_j]
                index_j += 1
            index_i += 1
            index_j = 0
        solution[1] = storage.index(-1)+1
        return solution



