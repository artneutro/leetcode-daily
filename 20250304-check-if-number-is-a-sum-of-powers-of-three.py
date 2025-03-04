# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = {}
        while n >= 3 :
            cum = 1
            while cum <= n :
                cum *= 3
            if cum == n :
                return True
            else :
                new_power = int(cum/3)
                if new_power in powers :
                    return False
                else :
                    powers[new_power] = True
                n = n-new_power
        if n == 0 or n == 1 or n == 3 :
            return True
        return False
