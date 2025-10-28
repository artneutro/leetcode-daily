# https://leetcode.com/problems/make-array-elements-equal-to-zero/
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        solution = 0
        index = 0
        while index < len(nums) :
            if nums[index] == 0 :
                sum_pre = sum(nums[:index])
                sum_pos = sum(nums[index+1:])
                if sum_pre == sum_pos :
                    solution += 2
                elif sum_pre == sum_pos-1 or sum_pre-1 == sum_pos :
                    solution += 1
            index += 1
        return solution
        
