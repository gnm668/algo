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
# print(x.values())


# def hasSingleCycle(array):
#     pos = 0
#     visit = {}
#     count = 0

#     while count < len(array) + 1:
#         visit[pos] = True
#         if count == 0:
#             visit.pop(0)
#         pos = (pos + array[pos]) % len(array)
#         count += 1
#     if len(visit.values()) == len(array):
#         return True
#     return False

# Below has better space complexity but same time complexity

def hasSingleCycle(array):
    visitedCount = 0
    currentPos = 0

    while visitedCount < len(array):
        if visitedCount > 0 and currentPos == 0:
            return False
        visitedCount += 1
        currentPos = getNextPos(currentPos, array)
    return currentPos == 0

def getNextPos(currentPos, array):
    move = array[currentPos]
    nextPos = (currentPos + move) % len(array)
    return nextPos if nextPos >= 0 else nextPos + len(array)

# def balancedBrackets(string):
#     opening = '({['
# 	closing = ')}]'
# 	stack = []
	
# 	if len(string) == 0:
# 		return False

# 	for bracket in string:
# 		if bracket in closing:
# 			if len(stack) != 0:
# 				if opening.index(stack[-1]) == closing.index(bracket):
# 					stack.pop()
# 				else:
# 					return False
# 			else:
# 				return False
# 		elif bracket in opening:
# 			stack.append(bracket)
# 	if len(stack) == 0:
# 		return True
# 	else:
# 		return False

def balancedBrackets(string):
    opening = '({['
    closing = ')}]'
    matching = {')':'(', '}':'{', ']':'[' }
    stack = []

    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            elif stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAddress = []
        for char in address:
            if char == '.':
                newAddress.append('[.]')
            else:
                newAddress.append(char)
        return ''.join(newAddress)
