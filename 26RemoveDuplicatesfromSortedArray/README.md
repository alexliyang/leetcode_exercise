# 思路
## 思路1

- 描述：类似27题，需要额外定义一个指针k，来使得[0,...k)位置为唯一值。由于数组是有序的，遍历数组，当遇到相邻两个元素不一致时，把后者放入[0,...k)的区间内，直到遍历结束。
- 时间复杂度：O(n)
- 空间复杂度：O(1)
- 注意点：k从1开始，因为有序，第一个数不用判断。同时注意空数组的判断，返回0。


## 思路2

- 描述：同样使用指针k，对数组进行遍历，判断当前值是否与k指针指的值相等。
- 时间复杂度：O(n)
- 空间复杂度：O(1)