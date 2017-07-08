class Solution(object):
# 思路1
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonZeros = []
        for n in nums:
            if n != 0:
                nonZeros.append(n)
        
        nums[:len(nonZeros)] = nonZeros
        
        nums[len(nonZeros):] = [0] * (len(nums) - len(nonZeros))
            
        