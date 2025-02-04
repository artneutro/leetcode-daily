# https://leetcode.com/problems/maximum-ascending-subarray-sum/
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        if len(nums) == 1 :
            return nums[0]
        index = 0
        highe = 0
        accum = nums[index]
        while index < len(nums)-1 :
            if nums[index+1] > nums[index] :
                accum += nums[index+1]
            else :
                if accum > highe :
                    highe = accum
                accum = nums[index+1]
            index += 1
        if accum > highe :
            highe = accum
        return highe
