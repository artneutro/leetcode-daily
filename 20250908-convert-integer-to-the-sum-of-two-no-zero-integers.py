# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n-1
        b = 1
        while a >= b :
            if '0' not in str(a) and '0' not in str(b) :
                return [a,b]
            a -= 1
            b += 1
        return -1
