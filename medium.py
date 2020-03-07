# def searchInSortedMatrix(matrix, target):
#     for row in range(len(matrix)):
# 	    for col in range(len(matrix[0])):
# 	        if matrix[row][col] == target:
# 	            return [row, col]
# 	return [-1, -1]

# def searchInSortedMatrix(matrix, target):
#     row = 0
#     col = len(matrix[0]) - 1

#     while row < len(matrix) and col >= 0:
#         if matrix[row][col] > target:
#             col -= 1
#         elif matrix[    row][col] < target:
#             row += 1
#         else:
#             return [row, col]
#     return [-1, -1]

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

# def smallestDifference(arrayOne, arrayTwo):
#     idxOne = 0
#     idxTwo = 0
#     arrayOne.sort()
#     arrayTwo.sort()
#     diff = float('inf')
#     curr = float('inf')
#     pair = []

#     while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
#         firstNum = arrayOne[idxOne]
#         secondNum = arrayTwo[idxTwo]

#         if firstNum < secondNum:
#             curr = secondNum - firstNum
#             idxOne += 1
#         elif firstNum > secondNum:
#             curr = firstNum - secondNum
#             idxTwo +=1
#         else:
#             return [firstNum, secondNum]
#         if diff > curr:
#             diff = curr
#         pair =[firstNum, secondNum]

#     return pair

# x = {1: None, 2: 2, 3: 3}
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

# def hasSingleCycle(array):
#     visitedCount = 0
#     currentPos = 0

#     while visitedCount < len(array):
#         if visitedCount > 0 and currentPos == 0:
#             return False
#         visitedCount += 1
#         currentPos = getNextPos(currentPos, array)
#     return currentPos == 0

# def getNextPos(currentPos, array):
#     move = array[currentPos]
#     nextPos = (currentPos + move) % len(array)
#     return nextPos if nextPos >= 0 else nextPos + len(array)

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

# def balancedBrackets(string):
#     opening = '({['
#     closing = ')}]'
#     matching = {')':'(', '}':'{', ']':'[' }
#     stack = []

#     for char in string:
#         if char in opening:
#             stack.append(char)
#         elif char in closing:
#             if len(stack) == 0:
#                 return False
#             elif stack[-1] == matching[char]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0


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

# x = { 1:'a', 2:'b'}
# print(a[:])
# a[0] = 100
# print(a)


# def minChange(coins, amount):
#     table = [float('inf')] * (amount + 1)
#     table[0] = 0

#     for coin in coins:
#         for amt in range(len(table)):
#             qty = 0 
#             while coin * qty <= amt:
#                 remainder = amt - (coin * qty)
#                 attempt = table[remainder] + qty
#                 if attempt < table[amt]: table[amt] = attempt
#                 qty += 1
#     return table[-1]

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

# def smallestDiff(li1, li2):
#     li1.sort()
#     li2.sort()
#     idx1, idx2 = 0, 0
#     curr, diff = float('inf'), float('inf')
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
#         if curr < diff:
#             diff = curr
#             pair = [num1, num2]
#     return pair       

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# def lucasNum(num, memo = {0: 2, 1: 1}):
#     if num in memo: return memo[num]
#     memo[num] = lucasNum(num -1) + lucasNum(num - 2)
#     return memo[num]

# def lucasNum(num):
#     table = [2, 1]
#     for i in range(num - 1):
#         temp = table[1]
#         table[1] = table[1] + table[0]
#         table[0] = temp
#     return table[1]
# print(lucasNum(40))

# def smallestDiff(li1, li2):
#     li1.sort()
#     li2.sort()
#     idx1, idx2 = 0, 0 
#     curr, diff = float('inf'), float('inf')
#     pair = []

#     while idx1 < len(li1) and idx2 < len(li2):
#         num1, num2 = li1[idx1], li2[idx2]
#         if num1 > num2:
#             curr = num1 - num2
#             idx2 += 1
#         elif num1 < num2:
#             curr = num2 - num1
#             idx1 += 1
#         else:
#             return [num1, num2]
#         if curr < diff:
#             diff = curr
#             pair = [num1, num2]
#     return pair

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

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

# class Node:
#     def __init__(self, name):
#         self.children = []
#         self.name = name
    
#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self

#     def printChildren(self):
#         for child in self.children:
#             print(child.name)

    # def bfs(self, array = []):
    #     queue = [self]
    #     while len(queue) > 0:
    #         current = queue.pop(0)
    #         array.append(current.name)
    #         for child in current.children:
    #             queue.append(child)
    #     return array

# class Node:

#     def __init__(self, name):
#         self.children = []
#         self.name = name

#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self

#     def printChildren(self):
#         for child in self.children:
#             print(child.name)
    
#     def bfs(self, array):
#         queue = [self]
#         while len(queue) > 0:
#             curr = queue.pop(0)
#             array.append(curr.name)
#             for child in curr.children:
#                 queue.append(child)
#         return array

# tree = Node('A')
# tree.addChild('B')
# tree.addChild('C')
# tree.children[0].addChild('D')
# tree.children[0].addChild('E')
# tree.children[1].addChild('F')

# print(tree.bfs([]))

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

# def smallestDiff(li1, li2):
#     li1.sort()
#     li2.sort()
#     idx1, idx2 = 0, 0
#     curr, diff = float('inf'), float('inf')
#     pair = []

#     while idx1 < len(li1) and idx2 < len(li2):
#         num1, num2 = li1[idx1], li2[idx2]
#         if num1 > num2:
#             curr = num1 - num2
#             idx2 += 1
#         elif num1 < num2:
#             curr = num2 - num1
#             idx1 += 1
#         else:
#             return [num1, num2]
#         if curr < diff:
#             diff = curr
#             pair = [num1, num2]
#     return pair
            
# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# def minChange(coins, amount, memo = {}):
#     if amount == 0: return 0
#     if amount in memo: return memo[amount]
#     numCoins = []
#     for coin in coins:
#         if coin <= amount:
#             numCoins.append(minChange(coins, amount - coin, memo) + 1)
#     memo[amount] = min(numCoins)
#     return memo[amount]

# def minChange(coins, amount):
#     table = [float('inf')] * (amount + 1)
#     table[0] = 0
#     for coin in coins:
#         for amt in range(len(table)):
#             qty = 0
#             while qty * coin <= amount:
#                 remainder = amount - (qty * coin)
#                 attempt = table[remainder] + qty
#                 if attempt < table[amt]: table[amt] = attempt
#                 qty += 1
    
#     return table[-1]


# print(minChange([1, 2, 5], 10))

# def smallestDiff(li1, li2):
#     li1.sort()
#     li2.sort()
#     curr, diff = float('inf'), float('inf')
#     idx1, idx2 = 0, 0
#     pair = []
#     while idx1 < len(li1) and idx2 < len(li2):
#         num1, num2 = li1[idx1], li2[idx2]
#         if num1 < num2:
#             curr = num2 - num1
#             idx1 += 1
#         elif num1 > num2:
#             curr = num1 - num2
#             idx2 += 1
#         else:
#             return [num1, num2]
#         if curr < diff:
#             diff = curr
#             pair = [num1, num2]
#     return pair

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []
    
#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self
    
#     def bfs(self, array):
#         queue = [self]
#         while len(queue) > 0:
#             curr = queue.pop(0)
#             array.append(curr.name)
#             for child in curr.children:
#                 queue.append(child)
#         return array

# tree = Node('A')
# tree.addChild('B')
# tree.addChild('C')
# tree.children[0].addChild('D')
# tree.children[0].addChild('E')
# tree.children[1].addChild('F')

# print(tree.bfs([]))

# def minChange(coins, amount, memo = {}):
#     if amount in memo: return memo[amount]
#     if amount == 0: return 0
#     numCoins = []
#     for coin in coins:
#         if coin <= amount:
#             numCoins.append(minChange(coins, amount - coin, memo) + 1)
#     memo[amount] = min(numCoins)
#     return memo[amount]

# def minChange(coins, amount):
#     table = [float('inf')] * (amount + 1)
#     table[0] = 0
#     for coin in coins:
#         for amt in range(len(table)):
#             qty = 0
#             while qty * coin <= amt:
#                 remainder = amt - (coin * qty)
#                 attempt = table[remainder] + qty
#                 if attempt < table[amt]: table[amt] = attempt
#                 qty += 1
#     return table[-1]

# print(minChange([1, 2, 5], 10))

# def threeSum(li, tar):
#     li.sort()
#     res = []
#     for i in range(len(li)):
#         left = i + 1
#         right = len(li) - 1
#         while left < right:
#             currSum = li[i] + li[left] + li[right]
#             if currSum == tar:
#                 res.append([li[i], li[left], li[right]])
#                 right -= 1
#                 left += 1
#             elif currSum > tar:
#                 right -= 1
#             elif currSum < tar:
#                 left += 1
#     return res

# print(threeSum([6,2,1,3,5,6,0], 8))

# def smallestDiff(li1, li2):
#     li1.sort()
#     li2.sort()
#     idx1, idx2 = 0, 0
#     diff, curr = float('inf'), float('inf')
#     pair = []
#     while idx1 < len(li1) and idx2 < len(li2):
#         num1, num2 = li1[idx1], li2[idx2]
#         if num1 > num2:
#             curr = num1 - num2
#             idx2 += 1
#         elif num1 < num2:
#             curr = num2 - num1
#             idx1 += 1
#         else:
#             return [num1, num2]
#         if curr < diff:
#             diff = curr
#             pair = [num1, num2]
#     return pair

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# def moveElementToEnd(li, toMove):
#     i = 0
#     j = len(li) - 1
#     while i < j:
#         while i < j and li[j] == toMove:
#             j -= 1
#         if li[i] == toMove:
#             li[i], li[j] = li[j], li[i]
#         i += 1
#     return li

# print(moveElementToEnd([2,1,2,2,2,4,3,2], 2))

# def gridSearch(grid, tar):
#     row = 0
#     col = len(grid[0]) - 1
#     while row < grid.length and col >= 0:
#         if grid[row][col] < tar:
#             row += 1
#         elif grid[row][col] > tar:
#             col += 1
#         else:
#             return [row, col]
#     return -1

# class MinMaxStack(self):
#     def __init__(self):
#         self.stack = []
#         self.minMaxStack = []
    
#     def peek(self):
#         return self.stack[-1]

#     def pop(self):
#         self.minMaxStack.pop()
#         return self.stack.pop()

#     def push(self, number):
#         newMinMax = {"min": number, "max": number}
#         if len(self.minMaxstack):
#             lastMinMax = self.minMaxStack[-1]
#             newMinMax["min"] = min(lastMinMax["min"], number)
#             newMinMax["max"] = max(lastMinMax["max"], number)
#         self.minMaxStack.append(newMinMax)
#         self.stack.append(number)
#         return self.stack
    
#     def getMin(self):
#         return MinMaxStack[-1]["min"]

#     def getMax(self):
#         return MinMaxStack[-1]["max"]

# def gridSearch(grid, tar):
#     row = 0
#     col = len(grid[0] - 1)

#     while row < len(grid) - 1 and col >= 0:
#         if grid[row][col] > tar:
#             col -= 1
#         elif grid[row][col] < tar:
#             row += 1
#         else:
#             return [row, col]
#     return -1

# def minChange(coins, amount):
#     table = [float('inf')] * (amount + 1)
#     table[0] = 0
#     for coin in coins:
#         for amt in range(len(table)):
#             qty = 0
#             while qty * coin <= amt:
#                 remain = amt - (qty * coin)
#                 attempt = table[remain] + qty
#                 if attempt < table[amt]: table[amt] = attempt
#                 qty += 1
#     return table[-1]

# print(minChange([1,2,5], 26))

# def riverSizes(matrix):
#     sizes = []
#     visited = [[False for value in row] for row in matrix]
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if visited[row][col]:
#                 continue
#             findSize(row, col, visited, matrix, sizes)
           
#     return sizes


# def findSize(row, col, visited, matrix, sizes):
#     size = 0
#     nodesToEx = [[row, col]]
#     while len(nodesToEx):
#         currNode = nodesToEx.pop()
#         row = currNode[0]
#         col = currNode[1]
#         if visited[row][col]:
#             continue
#         visited[row][col] = True
#         if matrix[row][col] == 0:
#             continue
#         size += 1
#         unvisitedNeighbors = getUnvisited(row, col, visited, matrix)
#         for neighbor in unvisitedNeighbors:
#             nodesToEx.append(neighbor)
#     if size is not None and size > 0:
#         sizes.append(size)


# def getUnvisited(row, col, visited, matrix):
#     unvisitedNeighbors = []
#     if row > 0 and not visited[row - 1][col]:
#         unvisitedNeighbors.append([row - 1, col])
#     if row < len(matrix) - 1 and not visited[row + 1][col]:
#         unvisitedNeighbors.append([row + 1, col])
#     if col > 0 and not visited[row][col - 1]:
#         unvisitedNeighbors.append([row, col - 1])
#     if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
#         unvisitedNeighbors.append([row, col + 1])
#     return unvisitedNeighbors

# print(riverSizes([
#     [1,0,0,1,0],
#     [1,0,1,0,0],
#     [0,0,1,0,1],
#     [1,0,1,0,1],
#     [1,0,1,1,0]
# ]))

# def moveElToEnd(li, toMove):
#     i = 0
#     j = len(li) - 1
#     while i < j:
#         while i < j and li[j] == toMove:
#             j -= 1
#         if li[i] == toMove:
#             li[i], li[j] = li[j], li[i]
#         i += 1
#     return li

# print(moveElToEnd([2,1,2,2,2,4,3,2], 2))

# def gridSearch(grid, tar):
#     row = 0
#     col = len(grid[0]) - 1
#     while row < len(grid) and col >= 0:
#         if tar > grid[row][col]:
#             col -= 1
#         elif tar < grid[row][col]:
#             row += 1
#         else:
#             return grid[row][col]
#     return -1

def powerSet(li):
    res = [[]]
    for i in range(len(li)):
        for j in range(len(res)):
            res.append(res[j] + [li[i]])
    return res
print(powerSet([1,2,3]))