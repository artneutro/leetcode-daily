# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        index = 0
        while index < len(words)-1 :
            if sorted(words[index]) == sorted(words[index+1]) :
                words=words[:index+1]+words[index+2:]
            else :
                index += 1
        return words
