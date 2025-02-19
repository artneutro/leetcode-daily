# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ['a', 'b', 'c']
        # Initial config
        queue = []
        queue.append('a')
        queue.append('b')
        queue.append('c')
        # Create other configs
        counter = 0
        while len(queue) > 0 :
            pos = queue.pop(0)
            # Count only if size found
            if len(pos) == n :
                counter += 1
                # Return if word found
                if counter == k :
                    return pos
            elif len(pos) > n :
                break
            # Look for all combinations and append in queue
            index = 0
            while index < len(happy) :
                if happy[index] != pos[-1] :
                    queue.append(pos+happy[index])
                index += 1
        return ''
