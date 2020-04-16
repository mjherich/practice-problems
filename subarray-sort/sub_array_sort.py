def subarraySort(array):
	# Track the biggest element in arr as we're looping
	biggest = float('-inf')

	# Track the smallest out of order element
	s = float('inf')
	s_idx = None
	# Track last out of order element idx
	l_idx = -1

	for i in range(len(array)):
		cur = array[i]
		if cur >= biggest:
			biggest = cur
		else:
			l_idx = i
			if cur <= s:
				s = cur
				s_idx = i

			
	# Find where smallest and biggest out of order elements needs to go
	out = [-1, l_idx]
	if s_idx is not None:
		print('Need to sort')
		for i in range(len(array)):
			cur = array[i]
			if s < cur:
				out[0] = i
				break
	return out


# Tests
arr1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(arr1)) # Expect [3,9]

arr2 = [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]
print(subarraySort(arr2)) # Expect [4,9]


arr3 = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
print(subarraySort(arr3)) # Expect [4,6]

arr4 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(subarraySort(arr4)) # Expect [-1,-1]
