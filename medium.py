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
        elif matrix[    row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]

    # If sorted check possible coparisons
    # O(n + m) Time
    # O(1) Space


# def threeNumberSum(array, targetSum):
	# array.sort()
	# results = []
	
	# anchor = 0
	# left = 1
	# right = len(array) - 1
	
	# while left == len(array)/2 :
	# 	currentSum = array[anchor] + array[left] + array[right]
	# 	if currentSum < targetSum:
	# 		left += 1
	# 	elif currentSum > targetSum:
	# 		right -= 1
	# 	elif currentSum == targetSum:
	# 		results.append([array[anchor], array[left], array[right]])
	# 	elif left >= right:
	# 		anchor += 1
	# 		left = anchor + 1
	# 		right = len(array) - 1
	# return results

    # def threeNumberSum(array, targetSum):
    #     array.sort()
    #     results = []

    #     for i in range(len(array) - 2):
    #         left = i + 1
    #         right = len(array) - 1
    #         while left < right:
    #             currentSum = array[i] + array[left] + array[right]
    #             if currentSum < targetSum:
    #                 left += 1
    #             elif currentSum > targetSum:
    #                 right -= 1 
    #             else: 
    #                 results.append([array[i], array[left], array[right]])
    #                 left += 1
    #                 right -= 1
    #     return results

def smallestDifference(arrayOne, arrayTwo):
    idxOne = 0
    idxTwo = 0
    arrayOne.sort()
    arrayTwo.sort()
    diff = float('inf')
    curr = float('inf')
    pair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            curr = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            curr = firstNum - secondNum
            idxTwo +=1
        else:
            return [firstNum, secondNum]
        if diff > curr:
            diff = curr
        pair =[firstNum, secondNum]

    return pair

x = {1: None, 2: 2, 3: 3}
print(x.values())


def hasSingleCycle(array):
    pos = 0
    visit = {}
    count = 0

    while count < len(array) + 1:
        visit[pos] = True
        if count == 0:
            visit.pop(0)
        pos = (pos + array[pos]) % len(array)
        count += 1
    if len(visit.values()) == len(array):
        return True
    return False
