# 思路
## 思路1

- 描述：同样的，这与26，27都属于一类题。主要是对重复元素进行剔除，并且原始数组都是有序的。但该题要求每个元素最多可以重复2次保存，所以此时要引入一个计数器cnt，用来判断当前元素重复了几次。每次迭代判断nums[k]是不是与nums[i]相等，如果相等，判断cnt是不是超过了2，如果超过了的话k不动，继续遍历下一个。如果nums[i]!=nums[k]，将cnt置为1，对新的数组进行重新计数。接着做上面的判断。直到遍历结束。
- 时间复杂度：O(n)
- 空间复杂度：O(1)
- 伪代码：
		
		if !nums:
			return 0 # 考虑空数组
			
	
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
			
			
# LeetCode上别人思路

## C++

	int removeDuplicates(vector<int>& nums) {
	    int i = 0;
	    for (int n : nums)
	        if (i < 2 || n > nums[i-2])
	            nums[i++] = n;
	    return i;
	}

## Java

	public int removeDuplicates(int[] nums) {
	    int i = 0;
	    for (int n : nums)
	        if (i < 2 || n > nums[i-2])
	            nums[i++] = n;
	    return i;
	}

## Python

	def removeDuplicates(self, nums):
	    i = 0
	    for n in nums:
	        if i < 2 or n > nums[i-2]:
	            nums[i] = n
	            i += 1
	    return i

## Ruby

	def remove_duplicates(nums)
	    i = 0
	    nums.each { |n| nums[(i+=1)-1] = n if i < 2 || n > nums[i-2] }
	    i
	end