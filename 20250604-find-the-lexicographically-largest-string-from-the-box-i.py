# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Check max - O(n)
        max_letter = sorted(word)[-1]
        # Get indexes - O(n)
        max_indexes = []
        index = 0
        while index < len(word) :
            if word[index] == max_letter :
                max_indexes.append(index)
            index += 1
        # Case numFriends == 1
        if numFriends == 1 :
            return word
        # Case len(word) <= numFriends
        if len(word) <= numFriends :
            return max_letter
        # Case len(word) > numFriends
        # Get number of extra characters to max
        extra = len(word)-numFriends
        # Create a list to store cumulative options
        possibilities = [max_letter]*len(max_indexes)
        # Check only the options that start with the max 
        index = 1
        while index <= extra :
            # Increment the instances where the max appears in the string
            internal_index = 0
            while internal_index < len(possibilities) :
                # Increase the segment if the index is shorter than the word last index - O(n)
                if max_indexes[internal_index]+index < len(word) :
                    possibilities[internal_index] += word[max_indexes[internal_index]+index]
                internal_index += 1
            index += 1
        # Return the max of all the possibilities - O(n)
        return max(possibilities)
