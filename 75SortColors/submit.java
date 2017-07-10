public class Solution {
    // 三路快排
    public void sortColors(int[] nums) {
        int zero = -1; // [0,...zero] == 0
        int two = nums.length; // [two, ... nums.length) == 2

        for(int i = 0; i < two; ){
            if ( nums[i] == 0 ){ // 交换zero后面那个数与当前的nums[i]
                int temp = nums[++zero];
                nums[zero] = nums[i];
                nums[i++] = temp;
            }else if (nums[i] == 2) { // 交换two前面那个数与当前的nums[i]
                int temp = nums[--two];
                nums[two] = nums[i];
                nums[i] = temp;
            }else { // 为1的时候不动
                i++;
            }
        }
    }
}