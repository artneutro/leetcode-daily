# https://leetcode.com/problems/water-bottles-ii/
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Initial state
        full = numBottles
        empty = 0
        drunk = 0
        # While the full+empty are more than numExchange
        while full+empty >= numExchange :
            # Exchange numExchange empty bottles with one full water bottle. 
            # Then, increase numExchange by one.
            if empty >= numExchange :
                full += 1
                empty -= numExchange
                numExchange += 1
            # Drink any number of full water bottles turning them into empty bottles.
            else :
                drunk += full
                empty += full
                full = 0
        return drunk+full
