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
        vowels_index = 0
        index = 0
        while index < len(s) :
            if s[index] in ['A','E','I','O','U','a','e','i','o','u'] :
                s = s[:index]+vowelss[vowels_index]+s[index+1:]
                vowels_index += 1
            index += 1
        return s
