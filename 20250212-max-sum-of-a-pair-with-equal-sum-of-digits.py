# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        output = -1
        global_sum = {}
        index = 0
        while index < len(nums) :
            local_sum = 0
            # Sum digits
            for digit in str(nums[index]) :
                local_sum += int(digit)
            # Update Hashmap
            if local_sum in global_sum :
                if len(global_sum[local_sum]) == 2 :
                    # Only store the 2 max values per sum
                    local_min = min(global_sum[local_sum])
                    if nums[index] > local_min :
                        if global_sum[local_sum][0] == local_min :
                            global_sum[local_sum][0] = nums[index] 
                        else :
                            global_sum[local_sum][1] = nums[index] 
                else :
                    global_sum[local_sum].append(nums[index])
            else :
                global_sum[local_sum] = [nums[index]]
            index += 1
        # Get max pair, if exists
        for val_max in global_sum.values() :
            if len(val_max) == 2 :
                if output < sum(val_max) :
                    output = sum(val_max)
        return output
