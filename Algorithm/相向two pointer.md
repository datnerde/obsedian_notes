# 模版
```python
# 相向双指针(patition in quicksort)
def partition(self, A, start, end):
	if start >= end:
		return
	
	left, right = start, end
	
	# key point 1: pivot is the value, not the index
	pivot = A[(start + end) // 2]
	
	# key point 2: every time you compare left & right, it should be
	# left <= right not left < right
	
	while left <= right:
		while left <= right and A[left] < pivot:
			left += 1
		while left <= right and A[right] > pivot:
			right -= 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
```
# Reverse型
- 反转字符
- 反转回文串
## 经典例题
- [[125. Valid Palindrome]]
- [[680. Valid Palindrome II]]
# Two Sums型
- Two Sums
- Three Sums
## 经典例题
- [[1. Two Sum]]
- [[15. 3Sum]]
# Partition 型
* 快速排序
* 颜色排序
## 经典例题
- [[31. Partition Array]]
- [[75. Sort Colours]]
