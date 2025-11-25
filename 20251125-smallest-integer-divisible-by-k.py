# https://leetcode.com/problems/smallest-integer-divisible-by-k/
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Repunit 1
        if k % 2 != 0 and k % 5 != 0 :
            counter = 1
            item = 1
            while item%k != 0 :
                item = ((item * 10) + 1) % k
                counter += 1
            return counter
        return -1
