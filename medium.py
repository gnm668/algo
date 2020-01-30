# def searchInSortedMatrix(matrix, target):
#     for row in range(len(matrix)):
# 	    for col in range(len(matrix[0])):
# 	        if matrix[row][col] == target:
# 	            return [row, col]
# 	return [-1, -1]

def searchInSortedMatrix(matrix, target):
    row = 0
	col = len(matrix[0]) - 1
	
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
		else:
			return [row, col]
	return [-1, -1]

    # If sorted check possible coparisons
    # O(n + m) Time
    # O(1) Space


def threeNumberSum(array, targetSum):
	array.sort()
	results = []
	
	anchor = 0
	left = 1
	right = len(array) - 1
	
	while left == len(array)/2 :
		currentSum = array[anchor] + array[left] + array[right]
		if currentSum < targetSum:
			left += 1
		elif currentSum > targetSum:
			right -= 1
		elif currentSum == targetSum:
			results.append([array[anchor], array[left], array[right]])
		elif left >= right:
			anchor += 1
			left = anchor + 1
			right = len(array) - 1
	return results