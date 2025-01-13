# https://leetcode.com/problems/minimum-length-of-string-after-operations/
class Solution:
    def minimumLength(self, s: str) -> int:
        solution = 0
        char_count = {}
        index = 0
        while index < len(s) :
            if s[index] in char_count :
                char_count[s[index]] += 1
            else :
                char_count[s[index]] = 1
            index += 1
        results = list(char_count.values())
        for item in results :
            if item%2 == 0 :
                solution += 2
            else :
                solution += 1
        return solution
