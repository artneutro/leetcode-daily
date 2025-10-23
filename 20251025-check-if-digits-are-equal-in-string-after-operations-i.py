# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2 :
            index = 0
            while index < len(s)-1 :
                s = s[:index] + str((int(s[index]) + int(s[index+1])) % 10) + s[index+1:]
                index += 1
            s = s[:-1]
        return s[0] == s[1]
