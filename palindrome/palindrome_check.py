def is_palindrome(string):
  # check if length is 0 or 1 and return true

  # convert string to all lowercase
  string = string.lower().replace(" ", "")

  # split the string into a list
  # For loop over length of string
  for i in range(len(string) // 2):
    j = len(string) - i - 1
    # if element at i and end-i does not match
    if string[i] != string[j]:
      return False
  
  return True



# Test
test_1 = 'racecar'
print(is_palindrome(test_1))  # True

test_2 = 'notapalindrome'
print(is_palindrome(test_2))  # False

test_3 = 'A Santa at Nasa'
print(is_palindrome(test_1))  # True