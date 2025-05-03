# https://leetcode.com/problems/push-dominoes/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Count each symbol - O(n)
        index = 0
        count_point = 0
        count_l = 0
        count_r = 0
        while index < len(dominoes) :
            if dominoes[index] == '.' :
                count_point += 1
            elif dominoes[index] == 'L' :
                count_l += 1
            elif dominoes[index] == 'R' :
                count_r += 1
            index += 1
        # Base cases - All '.'
        if count_point == len(dominoes):
            return dominoes
        # Base cases - All 'L'
        if count_l == len(dominoes):
            return dominoes
        # Base cases - All 'R'
        if count_r == len(dominoes):
            return dominoes
        # Rest of the cases - O(n)
        index = 0
        ini = 0
        count_dot = 0
        while index < len(dominoes) :
            if dominoes[index] == '.' :
                ini = index-1
                while index < len(dominoes) :
                    if dominoes[index] == '.' :
                        index += 1
                    else :
                        break
                # If it reaches the end and the last was 'R'
                if index >= len(dominoes) :
                    if dominoes[ini] == 'R' :
                        # Will never be -1 as this will be all dots (base case)
                        while ini < len(dominoes) :
                            dominoes = dominoes[:ini]+'R'+dominoes[ini+1:]
                            ini += 1
                    break
                # Case start and reached L
                if ini == -1 and dominoes[index] == 'L' :
                    ini = 0
                    while ini < index :
                        dominoes = dominoes[:ini]+'L'+dominoes[ini+1:]
                        ini += 1
                # Case start and reached R
                elif ini == -1 and dominoes[index] == 'R' :
                    ini = index
                # It didn't reaches the end
                elif dominoes[ini] == 'R' and dominoes[index] == 'R' :
                    while ini < index :
                        dominoes = dominoes[:ini]+'R'+dominoes[ini+1:]
                        ini += 1
                elif dominoes[ini] == 'R' and dominoes[index] == 'L' :
                    if index-ini-1 != 1 :
                        is_pair = ((index-ini-1)%2 == 0)
                        if is_pair :
                            mid = ini+int((index-ini-1)/2)
                            while ini <= mid :
                                dominoes = dominoes[:ini]+'R'+dominoes[ini+1:]
                                ini += 1
                            while ini < index :
                                dominoes = dominoes[:ini]+'L'+dominoes[ini+1:]
                                ini += 1
                        else :
                            mid = ini+int((index-ini-1)/2)
                            while ini <= mid :
                                dominoes = dominoes[:ini]+'R'+dominoes[ini+1:]
                                ini += 1
                            ini += 1
                            while ini < index :
                                dominoes = dominoes[:ini]+'L'+dominoes[ini+1:]
                                ini += 1
                    else :
                        ini = index
                elif dominoes[ini] == 'L' and dominoes[index] == 'L' :
                    while ini < index :
                        dominoes = dominoes[:ini]+'L'+dominoes[ini+1:]
                        ini += 1
                elif dominoes[ini] == 'L' and dominoes[index] == 'R' :
                    ini = index
            index += 1
        return dominoes









