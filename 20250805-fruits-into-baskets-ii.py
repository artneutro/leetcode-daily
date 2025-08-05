# https://leetcode.com/problems/fruits-into-baskets-ii/
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        solution = 0
        while len(fruits) > 0 :
            next_fruit = fruits.pop(0)
            index = 0
            baskets_size = len(baskets)
            while index < len(baskets) :
                if baskets[index] >= next_fruit :
                    baskets = baskets[:index]+baskets[index+1:]
                    break
                index += 1
            if index == baskets_size :
                solution += 1
        return solution

