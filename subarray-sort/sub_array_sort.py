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
		if cur > biggest:
			biggest = cur
			# print(f"new biggest {cur}")
		else:
			l_idx = i
			if cur <= s:
				print(f"new smallest out of order {cur}")
				s = cur
				s_idx = i

			
	# Find where smallest and biggest out of order elements needs to go
	out = [-1, l_idx]
	if s_idx is not None:
		print('Need to sort')
		for i in range(len(array)):
			cur = array[i]
			if s <= cur:
				print('Found smallest idx')
				out[0] = i
				break
	return out


# Tests
arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(arr)) # Expect [3,9]
