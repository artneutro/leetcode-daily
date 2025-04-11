# https://leetcode.com/problems/count-symmetric-integers/
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        solution = 0
        # O(n*x) where x is the max number of digits
        while low <= high :
            # Convert the string to a list of int + O(x) 
            str_low = list(int(i) for i in str(low))
            # Only check even sized
            if len(str_low)%2 == 0 :
                # Compare first half with second half
                if sum(str_low[:int(len(str_low)/2)]) == sum(str_low[int(len(str_low)/2):]) :
                    solution += 1
            low += 1
        return solution
