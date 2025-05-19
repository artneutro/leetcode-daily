# https://leetcode.com/problems/type-of-triangle/
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Equilateral
        if nums.count(nums[0]) == len(nums) :
            return 'equilateral'
        else :
            # Isosceles
            if nums[0] == nums[1] :
                if nums[0] + nums[1] > nums[2] :
                    return 'isosceles'
            elif nums[0] == nums[2] :
                if nums[0] + nums[2] > nums[1] :
                    return 'isosceles'
            elif nums[1] == nums[2] :
                if nums[1] + nums[2] > nums[0] :
                    return 'isosceles'
            # Scalene
            else :
                if nums[0] + nums[1] > nums[2]\
                and nums[0] + nums[2] > nums[1]\
                and nums[1] + nums[2] > nums[0] :
                    return 'scalene'
        return 'none'
