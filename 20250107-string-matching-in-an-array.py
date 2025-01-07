# https://leetcode.com/problems/string-matching-in-an-array/
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        solution = []
        index = 0
        while index < len(words) :
            next_sub = words[index]
            internal_index = 0
            while internal_index < len(words) :
                if index != internal_index :
                    if words[index] in words[internal_index] :
                        solution.append(words[index])
                internal_index += 1
            index += 1
        return list(set(solution))
