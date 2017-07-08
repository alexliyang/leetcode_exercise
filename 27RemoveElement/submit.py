class Solution(object):
    # 判断一下是不是有这个元素，没有的话就可以不用遍历了
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        if val in nums:
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[k] = nums[i]
                    k += 1
            return k
        else:
            return len(nums)
                
        