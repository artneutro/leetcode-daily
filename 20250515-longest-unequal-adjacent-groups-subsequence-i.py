# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        solution = []
        grp = -1
        index = 0
        while index < len(words) :
            if groups[index] != grp :
                solution.append(words[index])
                grp = groups[index]
            index += 1
        return solution
      
