# https://leetcode.com/problems/count-elements-with-maximum-frequency/
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        solution = 0
        max_freq = 0
        vals = {}
        for item in nums :
            if item in vals :
                vals[item] += 1
            else :
                vals[item] = 1
        index = 0 
        rep = list(vals.values())
        while index < len(rep) :
            if rep[index] > max_freq :
                max_freq = rep[index]
                solution = max_freq
            elif rep[index] == max_freq :
                solution += max_freq
            index += 1
        return solution
