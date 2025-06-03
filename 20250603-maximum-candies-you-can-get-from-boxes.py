# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Variables initialization
        solution = 0
        box_queue = []
        keys_found = {}
        # Iterate over initialBoxes to get initial boxes
        index_ini = 0
        while index_ini < len(initialBoxes) :
            box_queue.append((initialBoxes[index_ini], 0))
            index_ini += 1
        while len(box_queue) > 0 :
            next_box = box_queue.pop(0)
            # Check status or if the key was found
            if (status[next_box[0]] == 1) or (next_box[0] in keys_found) :
                # Check candies in box
                solution += candies[next_box[0]]
                # Check keys in box and store them
                for i in keys[next_box[0]] :
                    status[i] = 1
                # Check containedBoxes and enqueue them
                for i in containedBoxes[next_box[0]] :
                    box_queue.append((i, 0))
            else :
                # Stop if the box have been checked n times
                # Otherwise, re-enqueue it to see if the key is found later
                if next_box[1] < len(status) :      
                    box_queue.append((next_box[0], next_box[1]+1))
        return solution
