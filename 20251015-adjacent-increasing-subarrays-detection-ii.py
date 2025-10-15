# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        solution = 1
        ranges = []
        # Get all increased overall subarrays O(n)
        index = 0
        i_start = 0
        while index < len(nums)-1 :
            if nums[index] >= nums[index+1] :
                ranges.append([i_start, index+1])
                i_start = index + 1
            index += 1
        ranges.append([i_start, index+1])
        # O(n) => Worst case is decreasing array
        index = 0
        while index < len(ranges) : 
            half_len = int((ranges[index][1]-ranges[index][0])/2)
            # Check if current item has more than 2X size of current solution
            if half_len > solution :
                solution = half_len
            # Check if next item is adjacent 
            if index < len(ranges)-1 and ranges[index][1] == (ranges[index+1][0]) :
                min_len = min((ranges[index+1][1]-ranges[index+1][0]), (ranges[index][1]-ranges[index][0]))
                # If so, check min size and check if higher than solution
                if min_len > solution :
                    solution = min_len
            index += 1
        return solution
