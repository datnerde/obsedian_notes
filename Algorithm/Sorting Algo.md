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
# Merge Sort
- Expected Time Complexity: O(nlogn)
- Space Complexity: O(n)
```python
def sortintergers(self, A):
	if A == null or len(A) == 0:
		return
def MergeSort(self, A, start, end, temp):
	
```
# Bubble Sort