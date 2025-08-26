# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0.0
        max_diag = 0.0
        index = 0
        while index < len(dimensions) :
            cur_diag = math.sqrt((dimensions[index][0] * dimensions[index][0])\
                        + (dimensions[index][1] * dimensions[index][1]))
            cur_area = (dimensions[index][0] * dimensions[index][1]) 
            if cur_diag == max_diag :
                if cur_area > max_area :
                    max_area = cur_area
                max_diag = cur_diag
            elif cur_diag > max_diag :
                max_area = cur_area
                max_diag = cur_diag
            index += 1
        return max_area
        
