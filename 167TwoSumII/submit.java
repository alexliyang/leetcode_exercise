public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int i = 0; i < numbers.length; i++){
            int num = target - numbers[i];
            
            // 二分查找
            int l = i + 1;
            int r = numbers.length - 1; // 在[l, r]中间查找
            while(l <= r){
                int mid = l + (r-l)/2;
                if (numbers[mid] == num)
                    return new int[] {i+1, mid+1};
                else if (numbers[mid] < num)
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return new int[] {};
    }
}