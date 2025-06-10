# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
class Solution:
    def maxDifference(self, s: str) -> int:
        # Get quantities
        quantities = {}
        index = 0
        while index < len(s) :
            if s[index] in quantities :
                quantities[s[index]] += 1
            else :
                quantities[s[index]] = 1
            index += 1
        # Get max difference
        values = list(quantities.values())
        max_odd = 0
        min_eve = 101
        index = 0 
        while index < len(values) :
            if values[index]%2 == 0 :
                if values[index] < min_eve :
                    min_eve = values[index]
            else :
                if values[index] > max_odd :
                    max_odd = values[index]
            index += 1
        return max_odd-min_eve
