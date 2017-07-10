class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 定义索引
        i = 0
        j = len(numbers) - 1
        
        while True:
            if (numbers[i] + numbers[j] > target):
                j -= 1
            elif (numbers[i] + numbers[j] < target):
                i += 1
            else:
                return [i+1, j+1]