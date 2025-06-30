# https://leetcode.com/problems/longest-harmonious-subsequence/
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Store repetitions in hashmap - O(n)
        val_hashmap = {}
        index = 0
        while index < len(nums) :
            if nums[index] in val_hashmap :
                val_hashmap[nums[index]] += 1
            else :
                val_hashmap[nums[index]] = 1
            index += 1
        # Check max sum between neighbours - O(n)
        max_sum = 0
        unique_vals = sorted(list(val_hashmap.keys()))
        index = 0
        while index < len(unique_vals)-1 :
            if unique_vals[index+1] - unique_vals[index] == 1 :
                if val_hashmap[unique_vals[index+1]]\
                + val_hashmap[unique_vals[index]] > max_sum :
                    max_sum = val_hashmap[unique_vals[index+1]] \
                    + val_hashmap[unique_vals[index]]
            index += 1
        # Return max sum
        return max_sum
        
