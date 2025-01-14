# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        char_found = {}
        solution = []
        counter = 0
        index = 0
        while index < len(A) :
            if A[index] in char_found :
                counter += 1
                del char_found[A[index]] 
            else :
                char_found[A[index]] = True
            if B[index] in char_found :
                counter += 1
                del char_found[B[index]] 
            else :
                char_found[B[index]] = True
            solution.append(counter)
            index += 1
        return solution

