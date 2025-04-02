# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        solution = 0
        # 3 variables
        if len(nums) == 3 :
            if (nums[0]-nums[1])*nums[2] > 0 :
                return (nums[0]-nums[1])*nums[2]
            else :
                return 0
        # 1. Point to i, the next value
        # 2. Point to j, the lowest value from i to len(nums)
        # 3. Point to k, the highest value from j to len(nums)
        i = 0
        j = 1
        k = 2
        while i < len(nums)-2 :
            # Optimization: Move the i0 to avoid getting false k max closer to i
            i0 = i
            while i0 < len(nums)-2 :
                k = len(nums)-(nums[::-1].index(max(nums[i0+2:])))-1
                if nums[i+1:k] != [] :
                    j = i+1+nums[i+1:k].index(min(nums[i+1:k]))
                else :
                    j = i
                # If j == min(nums) and k == max(nums), check if i is max from 0 to j
                if i < j and j < k :
                    if (nums[i]-nums[j])*nums[k] > solution :
                        solution = (nums[i]-nums[j])*nums[k]
                i0 += 1
            i += 1
        return solution
