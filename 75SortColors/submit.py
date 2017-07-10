class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if len(nums) > 1:
        #     redCnt = 0
        #     whiteCnt = 0
        #     blueCnt = 0
        #     for n in nums:
        #         if n == 0:
        #             redCnt += 1
        #         if n == 1:
        #             whiteCnt += 1
        #         if n == 2:
        #             blueCnt += 1
        #     nums[:redCnt] = [0] * redCnt
        #     nums[redCnt: redCnt+whiteCnt] = [1] * whiteCnt
        #     nums[redCnt+whiteCnt:] = [2] * blueCnt
        if len(nums) > 1:
            cnt = [0] * 3
            
            for n in nums:
                assert n >= 0 and n <= 2
                cnt[n] += 1
                
            nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]