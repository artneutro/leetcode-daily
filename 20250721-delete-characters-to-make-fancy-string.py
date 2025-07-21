# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
class Solution:
    def makeFancyString(self, s: str) -> str:
        index = 1
        current = s[0]
        count = 1
        while index < len(s) :
            if s[index] == current :
                if count < 2 :
                    count += 1
                else :
                    s = s[:index] + s[index+1:]
                    index -= 1
            else :
                current = s[index]
                count = 1
            index += 1
        return s
