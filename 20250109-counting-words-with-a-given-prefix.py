# https://leetcode.com/problems/counting-words-with-a-given-prefix/
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        solution = 0
        for item in words:
            if item.startswith(pref) :
                solution += 1
        return solution
