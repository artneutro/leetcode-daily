# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Find all 1's and check minor x, minor y, major x, major y
        minor_i = len(grid)
        minor_j = len(grid[0])
        major_i = -1
        major_j = -1
        # Iterate over the grid
        index_i = 0
        while index_i < len(grid) :
            index_j = 0
            while index_j < len(grid[0]) :
                if grid[index_i][index_j] == 1 :
                    if index_i < minor_i :
                        minor_i = index_i
                    if index_i > major_i :
                        major_i = index_i
                    if index_j < minor_j :
                        minor_j = index_j
                    if index_j > major_j :
                        major_j = index_j
                index_j += 1
            index_i += 1
        # Get rectangle from these values
        side_x = major_i - minor_i + 1
        side_y = major_j - minor_j + 1
        return side_x * side_y
