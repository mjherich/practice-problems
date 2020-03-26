# Naive solution
def smallestDifference(arrayOne, arrayTwo):
    closest = int(9999999999999999999)
    closest_pair = []
    
    nums = set()
    for num in arrayOne:
    	for num2 in arrayTwo:
            if abs(num - num2) < closest:
                closest = abs(num - num2)
                closest_pair = [num, num2]

    return closest_pair

# Tests
arrOne = [-1, 5, 10, 20, 28, 3]
arrTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrOne, arrTwo)) # Expect [28, 26]