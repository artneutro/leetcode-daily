# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        solution = 0
        hashmap = {}
        # For each element xi
        global_index = 0
        while global_index < len(arr) :
        # 0. For each element xi-1
            local_index = 0
            while local_index < global_index :
        # 0.1. If the (xi-1 + xi) exists in H, Append [(xi, 2)] in H(xi-1 + xi)
                if (arr[local_index]+arr[global_index]) in hashmap :
                    hashmap[(arr[local_index]+arr[global_index])].append((arr[global_index], 2))
        # 0.2. If not, Insert the element as H(xi-1 + xi) = [(xi, 2)]
                else :
                    hashmap[(arr[local_index]+arr[global_index])] = [(arr[global_index], 2)]
                local_index += 1
        # 1. If the element xi exists in the Hashmap, for each element yi in the list:
            if arr[global_index] in hashmap :
                for item in hashmap[arr[global_index]] :
        # 1.1. If the (H(xi)[yi][0] + xi) exists in H, Append (xi, (H(xi)[yi][1])+1)) in H(H(xi)[yi][0] + xi)
                    if (item[0] + arr[global_index]) in hashmap :
                        hashmap[(item[0] + arr[global_index])].append((arr[global_index], item[1]+1))
        # 1.1.2. If (H(xi)[yi][1])+1) > solution; then solution = (H(xi)[yi][1])+1)
                        if item[1]+1 > solution :
                            solution = item[1]+1
            global_index += 1
        # Return the solution
        return solution
