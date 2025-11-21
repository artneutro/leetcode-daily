# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        solution = 0
        # O(k) where k is the number of different chars (max 26)
        for item in sorted(list(set(s))) :
            # First pointer to look for next char - O(n)
            index = 0
            while index < len(s)-2 :
                if s[index] == item :
                    comparator = len(s)-1
                    # Second pointer with regression - O(n)
                    while s[comparator] != item and index < comparator :
                        comparator -= 1
                    # Another set of solutions found
                    if comparator-index > 1 :
                        palin_subsequences = len(set(s[index+1:comparator]))
                        solution += palin_subsequences
                        break
                index += 1
        return solution
