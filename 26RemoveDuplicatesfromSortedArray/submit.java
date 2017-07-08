public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0)
            return 0;
        else{
            int k = 1;
            for(int i = 0; i < nums.length - 1; i++){
                if (nums[i+1] != nums[i])
                    nums[k++] = nums[i+1];
            }
            return k;
        }
    }
}