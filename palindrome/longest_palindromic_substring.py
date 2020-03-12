def longest_palindromic_substring(string):
	# convert string to all lowercase and remove spaces
	string = string.lower().replace(" ", "")

	# Keep track of longest substring palindrome
	longest = 0
	longest_ss = ""

	for i in range(len(string)):
		# Check odd length palindromes
		left = i
		right = i
		while True:
			# If substring is valid and is palindrome check to see if it's longest
			if left >= 0 and right < len(string) and string[left] == string[right]:
				cur_ss = string[left:right+1]
				if len(cur_ss) > longest:
					longest = len(cur_ss)
					longest_ss = cur_ss
			else:
				break
				
			# Update left and right cursors
			left -= 1
			right += 1
		
		# Check even length palindromes
		left = i
		right = i+1
		while True:
            # If substring is valid and is palindrome check to see if it's longest
			if right < len(string) and string[left] == string[right]:
				cur_ss = string[left:right+1]
				if len(cur_ss) > longest:
					longest = len(cur_ss)
					longest_ss = cur_ss
			else:
				break
			
			# Update left and right cursors
			left -= 1
			right += 1
		
	return longest_ss


# Test it
print(longest_palindromic_substring("abaxyzzyxf")) # Expect "xyzzyx"

print(longest_palindromic_substring("A Santa at Nasa not a palindrome")) # Expect "asantaatnasa"

print(longest_palindromic_substring("kayaking is fun")) # Expect "kayak"