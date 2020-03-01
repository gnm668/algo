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


# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         newAddress = []
#         for char in address:
#             if char == '.':
#                 newAddress.append('[.]')
#             else:
#                 newAddress.append(char)
#         return ''.join(newAddress)

#     def customSortString(self, S: str, T: str) -> str:
#         T = list(T)
#         T.sort(key=lambda a: S.index(a) if a in S else 0)
#         return ''.join(T)



# def quickSort(array):

#     if len(array) < 2:
#         return array 

#     pivot = array[0]
#     left = [el for el in array[1:] if el < pivot]
#     right = [el for el in array[1:] if el >= pivot]
#     return quickSort(left) + [pivot] + quickSort(right)
    
# a = [4, 4,3,2,1]
# b = 'hello'

# print(quickSort(a))


# x = lambda x: x + 2
# def isOdd(num):
#     if num % 2 != 0:
#         return True
#     else:
#         return False

# print(x(2))



# print(map(x, a))
# print([x(el) for el in a if el % 2 == 0])
# print(filter(isOdd, a))
# print([el for el in a if el % 2 == 0])
# print(b)

x = { 1:'a', 2:'b'}
# print(a[:])
# a[0] = 100
# print(a)


def minChange(coins, amount):
    table = [float('inf')] * (amount + 1)
    table[0] = 0

    for coin in coins:
        for amt in range(len(table)):
            qty = 0 
            while coin * qty <= amt:
                remainder = amt - (coin * qty)
                attempt = table[remainder] + qty
                if attempt < table[amt]: table[amt] = attempt
                qty += 1
    return table[-1]

# def minChange(coins, amount, memo = {}):
#     if amount == 0: return 0
#     numCoins = []
#     for coin in coins:
#         if coin <= amount:
#             numCoins.append(minChange(coins, amount - coin, memo) + 1)
#     memo[amount] = min(numCoins)
#     return memo[amount]

# print(minChange([1, 2, 5], 10))

# def quickSort(li):
#     if len(li) < 1: return li
#     pivot = li.pop()
#     left = [el for el in li if el <= pivot]
#     right = [el for el in li if el > pivot]
#     return quickSort(left) + [pivot] + quickSort(right)

# print(quickSort([5,4,3,2,1]))

# def threeSum(li, tar):
#     li.sort()
#     results = []
#     for i in range(len(li) - 2):
#         left = i + 1
#         right = len(li) - 1
#         while left < right:
#             currSum = li[i] + li[left] + li[right]
#             if currSum == tar:
#                 results.append([li[i], li[left], li[right]])
#                 left += 1
#                 right -= 1
#             elif currSum > tar:
#                 right -= 1
#             elif currSum < tar:
#                 left += 1
#     return results

# print(threeSum([6,2,1,3,5,6,0], 8))

# def smallestDifference(li1, li2):
#     idx1 = 0
#     idx2 = 0
#     li1.sort()
#     li2.sort()
#     curr = float('inf')
#     diff = float('inf')
#     pair = []

#     while idx1 < len(li1) and idx2 < len(li2):
#         num1 = li1[idx1]
#         num2 = li2[idx2]

#         if num1 < num2:
#             curr = num2 - num1
#             idx1 += 1
#         elif num1 > num2:
#             curr = num1 - num2
#             idx2 += 1
#         else:
#             return [num1, num2]
#         if diff > curr:
#             diff = curr
#             pair = [num1, num2]
#     return pair

# print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# def threeSum(li, tar):
#     li.sort()
#     res = []
#     for i in range(len(li) - 2):
#         left = i + 1
#         right = len(li) - 1
#         while left < right:
#             currSum = li[i] + li[left] + li[right]
#             if currSum == tar:
#                 res.append([li[i], li[left], li[right]])
#                 left += 1
#                 right -= 1
#             elif currSum > tar:
#                 right -= 1
#             elif currSum < tar:
#                 left += 1
#     return res

# print(threeSum([6,2,1,3,5,6,0], 8))

def smallestDiff(li1, li2):
    li1.sort()
    li2.sort()
    idx1, idx2 = 0, 0
    curr, diff = float('inf'), float('inf')
    pair = []
    while idx1 < len(li1) and idx2 < len(li2):
        num1 = li1[idx1]
        num2 = li2[idx2]
        if num1 < num2:
            curr = num2 - num1
            idx1 += 1
        elif num1 > num2:
            curr = num1 - num2
            idx2 += 1
        else:
            return [num1, num2]
        if curr < diff:
            diff = curr
            pair = [num1, num2]
    return pair       

print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
