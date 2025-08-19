# https://leetcode.com/problems/number-of-zero-filled-subarrays/
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        solution = 0
        # Gauss sum formulae
        index = 0
        current_count = 0
        while index < len(nums) :
            if nums[index] == 0 :
                current_count += 1
            else :
                if current_count > 0 :
                    solution += int(((current_count) * (current_count+1))/2)
                    current_count -= 1
                current_count = 0
            index += 1
        # Last items are 0-es
        if current_count > 0 :
            solution += int(((current_count) * (current_count+1))/2)
            current_count -= 1
        return solution
        
