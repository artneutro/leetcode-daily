# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True
        diffe = {}
        count = 0
        index = 0
        while index < len(s1) :
            if s1[index] != s2[index] :
                count += 1
                if s2[index] in diffe and diffe[s2[index]] == s1[index] :
                    del diffe[s2[index]]
                else:
                    diffe[s1[index]] = s2[index]
            if count > 2 :
                return False
            index += 1
        if len(diffe) > 0 :
            return False
        return True
