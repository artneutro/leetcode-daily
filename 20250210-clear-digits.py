# https://leetcode.com/problems/clear-digits/
class Solution:
    def clearDigits(self, s: str) -> str:
        last_char = []
        index = 0
        while index < len(s) :
            if (s[index]).isdigit() :
                if len(last_char) == 0 :
                    s = s[:index]+s[index+1:]
                else :
                    index_char = last_char.pop()
                    s = s[:index]+s[index+1:]
                    s = s[:index_char]+s[index_char+1:]
                    index -= 1
            else :
                last_char.append(index)
                index += 1
        return s
