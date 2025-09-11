# https://leetcode.com/problems/sort-vowels-in-a-string/
class Solution:
    def sortVowels(self, s: str) -> str:
        vowelss = []
        indexes = []
        # Locate vowels
        index = 0
        while index < len(s) :
            if s[index] in ['A','E','I','O','U','a','e','i','o','u'] :
                vowelss.append(s[index])
                indexes.append(index)
            index += 1
        # Sort vowels
        vowelss = sorted(vowelss)
        # Reassign vowels
        while len(indexes) > 0 :
            s = s[:indexes[0]]+vowelss[0]+s[indexes[0]+1:]
            indexes.pop(0)
            vowelss.pop(0)
        return s
