# Quick Sort
- Expected Time Complexity: O(nlogn)
- Worst Time Complexity: O(n^2)
	- when the sequence i s in reversed order
- Space Complexity: O(1)
```python
def QuickSort(self, A, start, end):
	if start >= end:
		return

	left, right = start, end
	pivot = A[(left + right) // 2]
	
```
# Merge Sort
# Bubble Sort