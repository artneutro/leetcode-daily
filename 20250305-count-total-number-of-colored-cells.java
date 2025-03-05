// https://leetcode.com/problems/count-total-number-of-colored-cells/
class Solution {
    public long coloredCells(int n) {
        // It just follows a pattern
        return ((long)((Math.pow(((n*2)-1),2))/2))+1 ;
    }
}
