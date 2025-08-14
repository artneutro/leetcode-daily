# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        solution = ""
        index = 0
        while index < len(num)-2 :
            if num[index] == num[index+1] \
            and num[index] == num[index+2] :
                if num[index:index+3] > solution :
                    solution = num[index:index+3]
            index += 1
        return solution
        
