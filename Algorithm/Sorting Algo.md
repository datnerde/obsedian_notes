# Quick Sort
- Expected Time Complexity: O(nlogn)
- Worst Time Complexity: O(n^2)
	- when the sequence i s in reversed order
- Space Complexity: O(1)
```python
def sortintegers(self, A):
	if A == null or len(A) == 0:
		return
	self.QuickSort(A, 0, len(A) - 1)
def QuickSort(self, A, start, end):
	# handle edge case
	if start >= end:
		return
		
	left, right = start, end
	# key 1: extract pivot as value not index
	pivot = A[(left + right) // 2]
	# key 2: when comparing left & right, use <=
	while left <= right:
		# key 3: when comparing with pivot, use < or >
		while left <= right and A[left] < pivot:
			left += 1
		while left <= right and A[right] > pivot:
			right -= 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
	# continue to quicksort for left part and right part
	self.QuickSort(A, start, right)
	self.QuickSort(A, left, end)
```

[5,3,2,1,3]  3
[1,2,3,3,3]
[2,3,5,3]

![[Pasted image 20230903150133.png]]
# Merge Sort
- Expected  / Worst Time Complexity: O(nlogn)
- Space Complexity: O(n)
```python
def sortintergers(self, A):
	if A == null or len(A) == 0:
		return
	temp = [0]*len(A)
	self.MergeSort(A, 0, len(A) - 1, temp)
def MergeSort(self, A, start, end, temp):
	if start >= end:
		return
	self.MergeSort(A, start, (start + end) // 2, temp)
	self.MergeSort(A, (start + end) // 2 + 1, end, temp)
	self.merge(A, start, end, temp)
def merge(self, A, start, end, temp):
	middle = (start + end) // 2
	left_start = start
	right_start = middle + 1
	index = start
	while left_start <= middle and right_start <= end:
		if A[left_start] < A[right_start]:
			temp[index] = A[left_start]
			left_start += 1
			index += 1
		else:
			temp[index] = A[right_start]
			right_start += 1
			index += 1
	while left_start <= middle:
		temp[index] = A[left_start]
		index += 1
		left_start += 1
	while right_start <= end:
		temp[index] = A[right_start]
		index += 1
		right_start += 1
	for i in range(start, end + 1):
		A[i] = temp[i]
```