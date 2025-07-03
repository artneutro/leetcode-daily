# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        if k == 1 :
            return word[0]
        else :
            while len(word) < k :
                ini_len = 2*len(word)
                index = 0
                while len(word) < ini_len :
                    next_char = word[index]
                    if next_char == 'z' :
                        word += 'a'
                    else :
                        word += (chr(ord(next_char)+1))
                    index += 1
                if len(word) >= k :
                    return word[k-1]
        return word[k-1]
