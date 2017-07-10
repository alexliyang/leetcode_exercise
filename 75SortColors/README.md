# 思路
## 思路1

- 描述：我们要充分利用题目中的信息，即数组元素的取值为有限个，因此可以使用计数排序。遍历一遍数组，计算数组中有多少个0，多少个1，以及多少个2，再将这些数按照顺序插回去即可。
- 时间复杂度：O(n)
- 空间复杂度：O(k)，k为元素的取值范围

## 思路2

- 描述：三路快排。设置基准数zero与two，保证在整个过程中[0,...,zero]中的数都为0，[two,...,n-1]中的数都为2即可。设定i从0开始遍历数组，当遇到1时，i++。当遇到2时，将two-1对应位置的数和2交换，i不变。当遇到0时，将zero+1对应的数与0交换，由于zero+1位置的数一定是1，因此i++，遍历下一个。
- 时间复杂度：O(n)
- 空间复杂度：O(1)
- 优点：整个算法只对数组进行了一遍的遍历




作业：88，215