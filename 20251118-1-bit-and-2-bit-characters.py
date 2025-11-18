# https://leetcode.com/problems/1-bit-and-2-bit-characters/
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # Get rid of first zero batch
        index = 0
        while index < len(bits) and bits[index] == 0 :
            index += 1
        # Check starting from first one
        if len(bits[index:]) == 0 :
            return True
        else :
            while index < len(bits) :
                counter_ones = 0
                counter_zees = 0
                while index < len(bits) and bits[index] == 1 :
                    counter_ones += 1
                    index += 1
                # If odd, then add next zero
                if counter_ones%2 == 1 :
                    index += 1
                while index < len(bits) and bits[index] == 0 :
                    counter_zees += 1
                    index += 1
                if index == len(bits) :
                    # If it reached the end after compound with 1
                    if counter_zees == 0 :
                        return False
                    else :
                        return True
        return False
