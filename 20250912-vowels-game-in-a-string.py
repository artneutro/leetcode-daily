# https://leetcode.com/problems/vowels-game-in-a-string/
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Alice only loses if 0 vowels
        for i in s :
            if i.lower() in ['a', 'e', 'i', 'o', 'u'] :
                return True
        return False
