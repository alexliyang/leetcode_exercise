class Solution(object):
    # 思路：遍历数组，设置一个计数器，对同一个数字进行计数，同时设置k指针负责最终结果的索引。
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        k = 0
        cnt = 1
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[k]):
                cnt = 1 # 将cnt重置
                k += 1 # 移动指针
                nums[k] = nums[i]
            else: # 当两个数相等时
                if cnt < 2: # 重复值还没超过2
                    cnt += 1 # 计数增加
                    k += 1 # 移动指针
                    nums[k] = nums[i]
        
        return k+1