# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        solution = 0
        index = 0
        while index < len(words) :
            internal_index = index+1
            while internal_index < len(words) :
                if words[internal_index].startswith(words[index])\
                and words[internal_index].endswith(words[index]) :
                    solution += 1
                internal_index += 1
            index += 1
        return solution
        
