# https://leetcode.com/problems/maximum-difference-between-increasing-elements/
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        solution = -1
        max_after = max(nums)
        index = 0
        while index < len(nums) :
            current_min = nums[index] 
            if current_min >= max_after :
                if index+1 < len(nums) :
                    max_after = max(nums[index+1:])
            else :
                if max_after-current_min > solution :
                    solution = max_after-current_min
            index += 1
        return solution

