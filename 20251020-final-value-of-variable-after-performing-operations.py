# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        solution = 0
        index = 0
        while index < len(operations) :
            if operations[index] == '++X' or operations[index] == 'X++' :
                solution += 1
            else :
                solution -= 1
            index += 1
        return solution
        
