# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
class Solution:
    def maxOperations(self, s: str) -> int:
        solution = 0
        zer_end = (s[-1]=='0')
        cur_seq = 0
        cur_mul = 1
        # First sequence
        index = len(s)-1
        if not zer_end :
            while index >= 0 :
                if s[index] == '0' :
                    break
                index -= 1
        # Rest
        while index >= 0 :
            if s[index] == '1' :
                while index >= 0 and s[index] == '1' :
                    cur_seq += 1
                    index -= 1
                solution += cur_mul*cur_seq
                cur_seq = 0
                cur_mul += 1
            index -= 1
        return solution
        
