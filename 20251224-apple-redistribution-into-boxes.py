# https://leetcode.com/problems/apple-redistribution-into-boxes/
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        all_apples = sum(apple)
        sorted_box = sorted(capacity, reverse=True)
        index = 0
        while index < len(sorted_box) :
            if all_apples-sorted_box[index] <= 0 :
                return index + 1
            all_apples -= sorted_box[index]
            index += 1
        return len(sorted_box)+1
