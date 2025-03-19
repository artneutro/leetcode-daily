// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
class Solution {
    public int minOperations(int[] nums) { 
        int solution = 0;
        // Check how many 0 it has
        int zeroes_count = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0) {
                zeroes_count ++;
            }
        }
        // Base cases - all zeroes
        if (zeroes_count == nums.length) {
            if (nums.length%3 == 0) {
                return (int)(zeroes_count/3);
            }
            else {
                return -1;
            }
        }
        // Other cases
        int index = 0;
        while (index < nums.length-2) {
            if (nums[index] == 0) {
                int internal_index = index;
                while (internal_index < index + 3) {
                    if (nums[internal_index] == 0) {
                        nums[internal_index] = 1;
                    }
                    else {
                        nums[internal_index] = 0;
                    }
                    internal_index ++;
                } 
                solution ++;
            } 
            index ++;
        }
        // Check last 3 elements and must be all ones
        if (nums[nums.length-3]+nums[nums.length-2]+nums[nums.length-1] != 3){
            return -1;
        }   
        return solution;
    }
}
