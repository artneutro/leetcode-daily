# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2 :
            return False
        sorted_nums = sorted(nums)
        # The target must be half of the sum
        sum_nums = sum(nums)
        if sum_nums%2 != 0 : 
            return False
        target = int(sum_nums/2)
        # Test all possibilities
        index = len(nums)-1
        possible = {}
        possible[sorted_nums[0]] = sorted_nums[0]
        # Cases where values larger than half the sum exists => False
        if sorted_nums[index] > target :
            return False
        # Base case 
        elif sorted_nums[index] == target : 
            return True
        # Rest of cases
        while index > 0 :
            cur_val = list(possible.keys())
            for i in cur_val :
                # Solution found
                if i + sorted_nums[index] == target :
                    return True
                elif i + sorted_nums[index] < target :
                    # Store only if sum already not in hashtable
                    if i + sorted_nums[index] not in possible :
                        possible[i + sorted_nums[index]] = i + sorted_nums[index]
            index -= 1
        return False




