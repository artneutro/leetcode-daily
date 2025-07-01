# https://leetcode.com/problems/find-the-original-typed-string-i/
class Solution:
    def possibleStringCount(self, word: str) -> int:
        solution = 1
        # O(n)
        index = 1
        while index < len(word) :
            if word[index] == word[index-1] :
                solution += 1
            index += 1
        return solution
