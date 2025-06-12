# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = -101
        index = 0
        while index < len(nums)-1 :
            if abs(nums[index]-nums[index+1]) > max_diff :
                max_diff = abs(nums[index]-nums[index+1])
            index += 1
        if abs(nums[-1]-nums[0]) > max_diff :
            max_diff = abs(nums[-1]-nums[0])
        return max_diff

        
