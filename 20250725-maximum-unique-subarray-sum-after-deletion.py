# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sorted_and_uniq = sorted(list(set(nums)))[::-1]
        solution = sorted_and_uniq[0]
        index = 1
        while index < len(sorted_and_uniq) :
            if solution + sorted_and_uniq[index] > solution :
                solution += sorted_and_uniq[index]
            else :
                break
            index += 1
        return solution 
        
