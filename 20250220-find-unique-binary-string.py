# https://leetcode.com/problems/find-unique-binary-string/
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        initial_config = '0'*len(nums[0])
        global_index = 0
        local_index = 0
        while global_index < len(initial_config) :
            if initial_config not in nums :
                return initial_config
            while local_index < len(initial_config) :
                # Check variations in each digit
                if initial_config[:local_index]+'1'+initial_config[local_index+1:] not in nums :
                    return initial_config[:local_index]+'1'+initial_config[local_index+1:]
                local_index += 1
            initial_config = initial_config[:global_index]+'1'+initial_config[global_index+1:]
            global_index += 1
