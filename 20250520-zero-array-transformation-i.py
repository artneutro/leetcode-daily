# https://leetcode.com/problems/zero-array-transformation-i/
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool :
        solution = [0]*(len(nums)+1)
        # Base case: Max num is larger than all queries - O(n)
        max_nums = max(nums)
        if max_nums > len(queries) :
            return False
        # Iterate over the queries and increment/decrement based on the ranges - O(m)
        index = 0
        while index < len(queries) :
            next_range = queries[index]
            ini = next_range[0]
            end = next_range[1]
            # O(1)
            solution[ini] += 1
            solution[end+1] -= 1
            index += 1
        # Difference arrays - O(n)
        index = 1
        while index < len(solution) :
            solution[index] += solution[index-1]
            index += 1
        # Check possibility - O(n)
        index = 0
        while index < len(nums) :
            if nums[index]-solution[index] > 0 :
                return False
            index += 1
        return True
