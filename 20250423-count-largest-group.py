# https://leetcode.com/problems/count-largest-group/
class Solution:
    def countLargestGroup(self, n: int) -> int:
        solution = {}
        for i in range(1, n+1) :
            val = sum(int(j) for j in str(i))
            if val in solution :
                solution[val] += 1
            else :
                solution[val] = 1
        values_list = list(solution.values())
        return values_list.count(max(values_list))
