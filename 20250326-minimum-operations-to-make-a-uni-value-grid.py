# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        solution = 0
        # Sort 
        sorted_grid = sorted([j for i in grid for j in i])
        # Base cases
        # 1. Only 1 element - O(1)
        if len(sorted_grid) == 1 :
            return 0
        # 2. All are equal already (min and max are the same) - O(m*n)
        min_v = min(sorted_grid)
        max_v = max(sorted_grid)
        if min_v == max_v :
            return 0
        # 3. x is even and there are odd and even values - O(m*n)
        even = False
        odd = False
        x_even = (x%2 == 0)
        if x_even :
            index = 0
            while index < len(sorted_grid):
                if sorted_grid[index]%2 == 0 :
                    even = True
                    if odd and x_even :
                        return -1
                else : 
                    odd = True
                index += 1
        # Check what is the element in the middle
        mid = sorted_grid[int(len(sorted_grid)/2)]
        # For every element, check how many times to add or remove x
        hashtab = {}
        index = 0 
        while index < len(sorted_grid) :
            if sorted_grid[index] in hashtab :
                solution += hashtab[sorted_grid[index]]
            else :
                max_comp = max(sorted_grid[index],mid)
                min_comp = min(sorted_grid[index],mid)
                cur_valu = 0
                while min_comp < max_comp :
                    min_comp += x
                    cur_valu += 1
                    solution += 1
                if min_comp != max_comp :
                    return -1
                hashtab[sorted_grid[index]] = cur_valu
            index += 1
        return solution







