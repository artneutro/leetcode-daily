# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        while x < n :
            x *= 3
        if x == n :
            return True
        else :
            return False
        return False
        
