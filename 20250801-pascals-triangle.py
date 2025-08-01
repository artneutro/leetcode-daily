# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]
        numRows -= 1
        while numRows > 0 :
            new_row = [1]
            index = 0
            while index+1 < len(solution[-1]) :
                new_row.append(solution[-1][index]+solution[-1][index+1])
                index += 1
            new_row.append(1)
            solution.append(new_row)
            numRows -= 1
        return solution
        
