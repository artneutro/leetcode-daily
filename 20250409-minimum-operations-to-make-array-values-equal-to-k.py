# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If there are elements lower than k - O(n)
        if min(nums) < k :
            return -1
        # Get a set from nums - O(n)
        set_nums = set(nums)
        # Base case where all are equals to k - O(1)
        if len(set_nums) == 1 and nums[0] == k :
            return 0
        # Otherwise - O(n)
        return sum(1 for i in set_nums if (i > k)) or -1
