public class Solution {
    // 思路2
    public void moveZeroes(int[] nums) {
        // space O(1)
        // time O(n)
        int k = 0; //在[0, ... k) 区间内存储所有非0元素
        for(int i = 0; i < nums.length; i++){
            if (nums[i] != 0) {
                nums[k] = nums[i];
                k++;
            }
        }
        for(int j = k;j < nums.length; j++){
            nums[j] = 0;
        }
    }
}