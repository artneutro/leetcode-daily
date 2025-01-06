https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        solution = [0]*len(boxes)
        index = 0
        while index < len(boxes) :
            internal_index = 0
            while internal_index < len(boxes) :
                solution[index] += abs(index-internal_index)*int(boxes[internal_index])
                internal_index += 1
            index += 1
        return solution
