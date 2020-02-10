# def getNthFib(n, memo = {}):
# 	if n in memo:
# 		return memo[n]

# 	if n == 1:
# 		return 0
# 	elif n == 2:
# 		return 1
# 	else: 
# 		memo[n] = getNthFib(n - 1) + getNthFib(n - 2)
# 		return memo[n]


# print(getNthFib(50))

# def getNthFib(n, memo = {1: 0, 2: 1}):
# 	if n in memo:
# 		return memo[n]
# 	else:
# 		memo[n] = getNthFib(n - 1) + getNthFib(n - 2)
# 		return memo[n]

# print(getNthFib(50))

# time O(2^n) without meomoize
# space O(n) -- recursion call stack without memoize
# time O(n) with memoize
# space O(n) with memoize
# if using memoize with base cases, can store base cases in memo hash

# def getNthFib(n):
# 	lastTwo = [0, 1]
# 	counter = 3

# 	while counter <= n:
# 		nextFib = lastTwo[0] + lastTwo[1]
# 		lastTwo[0] = lastTwo[1]
# 		lastTwo[1] = nextFib
# 		counter += 1

# 	return lastTwo[1] if n > 1 else lastTwo[0]

# print(getNthFib(50))

# time O(n)
# space O(1)

# def bubbleSort(array):
# 	isSorted = False
	
# 	while not isSorted:
# 		isSorted = True
		
# 		for i in range(0, len(array) - 1):
# 			if array[i] > array[i + 1]:
# 				array[i], array[i +1] = array[i +1], array[i]
# 				isSorted = False
# 	return array

# time O(n^2)
# space O(1)

# def insertionSort(array):	
# 	for i in range(1, len(array)):
# 		j = i 
# 		while j > 0 and array[j] < array[j - 1]:
# 			swap(j, j - 1, array)
# 			j -= 1
	
# 	return array

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]

# time O(n^2) unless already sorted O(n)
# space O(1)

# def caesarCipherEncryptor(string, key):
# 	alpha = list("abcdefghijklmnopqrstuvwxyz")
# 	newStr = []
# 	for i in range(0, len(string)):
# 		if i == ' ':
# 			newStr.append(' ')
# 		else:
# 			oldIdx = alpha.index(string[i])
# 			newIdx = (oldIdx + key) % 26
# 			newStr.append(alpha[newIdx])
	
# 	return ''.join(newStr)

# SYNTAX
# time O(n)
# space O(n)

# def selectionSort(array):
# 	for i in range(0, len(array)):
# 		sIdx = i
		
# 		for j in range(i + 1, len(array)):
# 			if array[sIdx] > array[j]:
# 				sIdx = j
			
# 		swap(sIdx, i, array)
		
# 	return array

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]


# def insertionSort(array):	
# 	for i in range(1, len(array)):
# 		j = i 
# 		while j > 0 and array[j] < array[j - 1]:
# 			array[j], array[j - 1] = array[j - 1], array[j]
# 			j -= 1
	
# 	return array

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]


# def findThreeLargestNumbers(array):
# 	large = [None, None, None]
# 	for n in array:
# 		update(large, n)
# 	return large

# def update(large, num):
# 	if large[2] is None or large[2] < num:
# 		shift(large, num, 2) 
# 	elif large[1] is None or large[1] < num:
# 		shift(large, num, 1)
# 	elif large(0) is None or large[0] < num:
# 		shift(large, num , 0)

# def shift(large, num , idx):
# 	for i in range(idx +1):
# 		if i == idx:
# 			array[i] = num
# 		else
# 			array[i] = array[i + 1]
			


# space O(1)
# time O(n)

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def containsNodeWithValue(self, value):
# 		node = self.head
# 		while node is not None and node.value != value:
# 			node = node.next
# 		return node is not None   

#     def remove(self, node):
# 		if node = self.head:
# 			self.head = self.head.next
# 		if node = self.tail:
# 			self.tail = self.tail.prev
# 		self.removeNodeBindings(node)

# 	def removeNodeBindings(node):
# 		if node.prev is not None:
# 			node.prev.next = node.next
# 		if node.next is not None:
# 			node.next.prev = node.prev
# 		node.next = None
# 		node.prev = None

#     def removeNodesWithValue(self, value):		
# 		node = self.head
# 		while node is not None:
# 			temp = node
# 			node = node.next
# 			if temp.value == value:
# 				self.remove(temp)		

# 	def insertNodeBefore(self, node, nodeToInsert):
# 		if self.head == nodeToInsert and self.tail == nodeToInsert:
# 			return
# 		self.remove(nodeToInsert)
# 		nodeToInsert.next = node
# 		nodeToInsert.prev = node.prev
# 		if node.prev is None:
# 			self.head = nodeToInsert
# 		else:
# 			node.prev.next = nodeToInsert
# 		node.prev = nodeToInsert	
		
#     def insertAfter(self, node, nodeToInsert):
# 		if self.head == nodeToInsert and self.tail == nodeToInsert:
# 			return
# 		self.remove(nodeToInsert)
# 		nodeToInsert.prev = node
# 		nodeToInsert.next = node.next
# 		if node.next is None:
# 			self.tail = nodeToInsert
# 		else:
# 			node.next.prev = nodeToInsert
# 		node.next = nodeToInsert

#     def setHead(self, node):
# 		if self.head is None:
# 			self.head = node
# 			self.tail = node
# 			return
# 		self.insertBefore(self.head, node)

#     def setTail(self, node):
# 		if self.head is None:
# 			self.setHead(node)
# 		self.insertAfter(self.tail, node)

# 	    def insertAtPosition(self, position, nodeToInsert):
# 		if position == 1:
# 			self.setHead(nodeToInsert)
# 			return
			
# 		node = self.head
# 		currentNode = 1
		
# 		while node is not None and currentNode != position:
# 			node = node.next
# 			currentNode += 1
# 		if node is not None:
# 			self.insertBefore(node, nodeToInsert)
# 		else: 
# 			self.setTail(nodeToInsert)	


# def bSearch(arr, tar):
# 	return bSearchHelper(arr, tar, 0, len(arr) - 1)

# def bSearchHelper(arr, tar, left, right):
# 	if left > right:
# 		return -1

# 	mid = (left + right) // 2
# 	pMatch = arr[mid]

# 	if tar == pMatch:
# 		return mid
# 	elif tar < pMatch:
# 		return bSearchHelper(arr, tar, 0, mid - 1)
# 	elif tar > pMatch:
# 		return bSearchHelper(arr, tar, mid + 1, right)

# def binarySearch(array, target):
# 	left = 0
# 	right = len(array) - 1
	
# 	while left <= right:
# 		mid = (left + right) // 2
# 		pMatch = array[mid]
# 		if target == pMatch:
# 			return mid
# 		elif target < pMatch:
# 			right = mid - 1
# 		elif target > pMatch:
# 			left = mid + 1
# 	return -1


# print(binarySearch([1,2,3,4,5,7,7,10], 11))

# print('hi')


# class Node:
# 	def __init__(self, name):
# 		self.children = []
# 		self.name = name

# 	def addChild(self, name):
# 		self.children.append(Node(name))
# 		return self

# 	def depthFirstSearch(self, array):
# 		array.append(self.name)
# 		for child in self.children:
# 			child.depthFirstSearch(array)
# 		return array

# O(logn) n is # of nodes in tree
# O(n) worst case if tree is one branch
# space O(d) depth of recursion 

# def findClosestValueInBst(tree, target):
# 	return helper(tree, target, float("inf"))

# def helper(tree, target, closest):
# 	if tree is None:
# 		return closest
# 	if abs(target - closest) > abs(target - tree.value):
# 		closest = tree.value
# 	if target < tree.value:
# 		return helper(tree.left, target, closest)
# 	elif target > tree.value:
# 		return helper(tree.right, target, closest)
# 	else:
# 		return closest

# def findClosestValueInBst(tree, target, closest = float("inf")):
# 	currNode = tree
# 	while currNode is not None:
# 		if abs(target - closest) > abs(target - currNode.value):
# 			closest = currNode.value
# 		if target < currNode.value:
# 			currNode = currNode.left
# 		elif target > currNode.value:
# 			currNode = currNode.right
# 		else:
# 			break
# 	return closest

# # iterative is O(1) space 

# def branchSums(root):
# 	sums = []
# 	calculateBranchSums(root, 0, sums)
# 	return sums

# def calculateBranchSums(node, runningSum, sums):
# 	if node is None:
# 		return
	
# 	newRunningSum = runningSum + node.value
# 	if node.left is None and node.right is None:
# 		sums.append(newRunningSum)
# 		return
		
# 	calculateBranchSums(node.left, newRunningSum, sums)
# 	calculateBranchSums(node.right, newRunningSum, sums)	


# def groupAnagrams(words):	
# 	groups = {} #O(WN) Space
	
# 	for word in words:  #O(N) Time
# 		sortedWord = "".join(sorted(word)) #O(Wlog(W) Time
# 		if sortedWord in groups:
# 			groups[sortedWord].append(word)
# 		else:
# 			groups[sortedWord] = [word]
			
# 	return groups.values() 


# def foo(arr, tar): 
# 	return sorted(arr, key = lambda x: x == tar)

x = [1,2,3,4,5,6]
y = len(x) - 1
# print(y)



# x[0], x[1] = x[1], x[0]

# print(x)



# MoveElementToEnd

# def moveElementToEnd(array, toMove):
# 	swapIdx = None
# 	for i in range(len(array)):
# 		if toMove == array[i]:
# 			swapIdx = i
# 		else:
# 			if swapIdx is not None:
# 				array[swapIdx], array[i] = array[i], array[swapIdx]
# 				swapIdx = i
# 	return array

# DOESN'T WORK FOR SOME EDGE CASES

# def moveElementToEnd(array, toMove):
# 	left = 0
# 	right = len(array) - 1

# 	while left < right:
# 		if array[left] == toMove:
# 			if array[right] != toMove:
# 				array[left], array[right] = array[right], array[left]
# 			else: 
# 				right -= 1
# 		else:
# 			left += 1

# 	return array


# print(moveElementToEnd([2,1,2,2,3,4,2], 2))

# def maxSubsetSumNoAdjacent(array):
# 	if len(array) == 0:
# 		return 0

# 	first = array[0]
# 	second = array[1]
	

# 	if len(array) % 2 == 0:
# 		lastIdx = len(array) - 1
# 		if array[lastIdx] > array[lastIdx - 1]:
# 			swap(lastIdx, lastIdx - 1, array)
# 			array.pop()

# 	for i in range(2, len(array)):
# 		if i % 2 == 0:
# 			first += array[i]
# 		else:
# 			second += array[i]

# 	return max(first, second)

# def swap(i, j, array):
# 	array[i], array[j] = array[j], array[i]

# def maxSubsetSumNoAdjacent(array):
# 	if not len(array):
# 		return 0
# 	elif len(array) == 1:
# 		return array[0]

# 	second = array[0]
# 	first = max(array[0], array[1])

# 	for i in range(2, len(array)):
# 		current = max(first, second + array[i])
# 		second = first 
# 		first = current
# 	return first

# x = [75, 105, 120, 75, 90, 135]

# print(maxSubsetSumNoAdjacent(x))

    
# def moveElementToEnd(array, toMove):
# 	left = 0 
# 	right = len(array) -1

# 	while left < right:
# 		if array[left] == toMove:
# 			if array[right] != toMove:
# 				array[left], array[right] = array[right], array[left]
# 			else:
# 				right -= 1
# 		else:
# 			left += 1
# 	return array

# print(moveElementToEnd([2,1,2,2,3,4,2], 2))

# def maxAdjSum(array):
# 	if not len(array):
# 		return 0
# 	elif len(array) == 1:
# 		return array[0]

# 	first = array[0]
# 	second = max(array[0], array[1])

# 	for i in range(2, len(array)):
# 		current = max(second, first + array[i])
# 		first = second
# 		second = current
# 	return second

# x = []

# print(maxAdjSum(x))

# def smallestDifference(arrayOne, arrayTwo):
	# idxOne = 0
	# idxTwo = 0
	# arrayOne.sort()
	# arrayTwo.sort()
	# diff = float('inf')
	# curr = float('inf')
	# pair = []
	
	# while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
	# 	firstNum = arrayOne[idxOne]
	# 	secondNum = arrayTwo[idxTwo]
		
	# 	if firstNum < secondNum:
	# 		curr = secondNum - firstNum
	# 		idxOne += 1
	# 	elif firstNum > secondNum:
	# 		curr = firstNum - secondNum
	# 		idxTwo +=1
	# 	else:
	# 		return [firstNum, secondNum]
	# 	if diff > curr:
	# 		diff = curr
	# 		pair =[firstNum, secondNum]
			
	# return pair

garden = [
		[5, 7, 8, 6, 3],
		[0, 0, 7, 0, 4], 
		[4, 6, 3, 4, 9], 
		[3, 1, 0, 5, 8]
	]


def hungryRabbit(array):
	rabbit = start(array) # [row, col]
	monch(array, rabbit)




	# START
	#grab greatest center value 
	#if length or height are even
	#key into array at int(len(array) / 2)
	#compare 2 or 4 values for starting point

# def start(array):

	# row1, col1, row2, col2 = None, None, None, None

	# if len(array) % 2 == 1:
	# 	row1 = int(len(array) / 2)
	# else:
	# 	row1 = int(len(array) / 2)
	# 	row2 = int((len(array) / 2) - 1)

	# if len(array[0]) % 2 == 1:
	# 	col1 = int(len(array[0]) / 2)
	# else:
	# 	col1 = int(len(array[0]) / 2)
	# 	col2 = int((len(array[0]) / 2) - 1)


	# square1, square2, square3, square4 = array[row1][col1], array[row1][col2], array[row2][col1], array[row2][col2]
	# greatest = max(square1, square2, square3, square4)
	# if square1 == greatest:
	# 	return [row1, col1]
	# elif square2 == greatest:
	# 	return [row1, col2]
	# elif square3 == greatest:
	# 	return [row2, col1]
	# elif square4 == greatest:
	# 	return [row2, col2]


def monch(array, start):  #start is also an array
	hungry = True
	startRow = start[0]
	startCol = start[1]
	carrotSum = array[startRow][startCol]
	currentSquare = start
	directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
	
	while hungry == True:
		nextSquareVal = float("-inf")
		for direction in directions:
			row = currentSquare[0] + direction[0]
			col = currentSquare[1] + direction[1]

			if row >= 0 and row < len(array) and col >= 0 and col < len(array[0]):
				if array[row][col] > nextSquareVal:
					nextSquareVal = array[row][col]
					currentSquare = [row, col]
			elif nextSquareVal == 0:
				hungry = False
		carrotSum += nextSquareVal
	return carrotSum


	# TRAVERSE
	#create direction array 
	#interate through direction array and check 
	#values of surrounding squares, save highest value and direction unless index num is less than 0
	#update running sum and current position
	#if all surrounding values are NULL or 0 return final sum

def start(array):
	row_options = [len(garden) // 2, len(garden) // 2]
	col_options = [len(garden[0]) // 2, len(garden[0]) // 2]

    # If even, 1st option is one less than half the length
	if len(garden) % 2 == 0:
		row_options[0] -= 1

	if len(garden[0]) % 2 == 0:
		col_options[0] -= 1

	max = 0
	row = None
	col = None

	for r_option in row_options:
		for c_option in col_options:
			if garden[r_option][c_option] > max:
				max = garden[r_option][c_option]
				row = r_option
				col = c_option

	return row, col

def hungry_rabbit_util(garden, row, col):
	max = 0
	next_row = None
	next_col = None

	for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
		if row + r >= 0 and row + r < len(garden) and \
				col + c >= 0 and col + c < len(garden[row]):
			if garden[row + r][col + c] > max:
				max = garden[row + r][col + c]
				next_row = row + r
				next_col = col + c

	carrots = garden[row][col]
	garden[row][col] = 0

	if max > 0 and next_row is not None and next_col is not None:
		carrots += hungry_rabbit_util(garden, next_row, next_col)

	return carrots

def hungry_rabbit(garden):
    if len(garden) == 0 or len(garden[0]) == 0:
        return 0

    # create a copy of the garden so we can mutate it
    copy = [g_row[:] for g_row in garden]
    row, col = start(copy)

    if row is None or col is None:
        return 0

    return hungry_rabbit_util(copy, row, col)

# print(hungry_rabbit(garden))

# for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
# 	print(x)
	
def maxNonAdjSum(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]

	first = array[0]
	second = max(array[0], array[1])

	for i in range(2, len(array)):
		current = max(second, first + array[i])
		first = second
		second = current

	return second


x = [75, 105, 120, 75, 90, 135]

print(maxNonAdjSum(x))


# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale. Given an array of integers representing the color of 
# each sock, determine how many pairs of socks with matching colors there are.

# For example, there are
# socks with colors . There is one pair of color and one of color . There are 
# three odd socks left, one of each color. The number of pairs is .

def sockMerchant(n, ar):
    pairCount = 0
    colorCount = {}

    for color in ar:
        if color not in colorCount:
            colorCount[color] = 1
        else:
            colorCount[color] += 1

    for key in colorCount:
        pairCount += (colorCount[key] // 2)

    return pairCount


# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention 
# to small details like topography. During his last hike he took exactly steps. 
# For every step he took, he noted if it was an uphill, , or a downhill, step. 
# Gary's hikes start and end at sea level and each step up or down represents a

# unit change in altitude. We define the following terms:

#     A mountain is a sequence of consecutive steps above sea level, starting with 
# 	a step up from sea level and ending with a step down to sea level.

#     A valley is a sequence of consecutive steps below sea level, starting with 
# 	a step down from sea level and ending with a step up to sea level.

# Given Gary's sequence of up and down steps during his last hike, find and print 
# the number of valleys he walked through.

# For example, if Gary's path is
# , he first enters a valley units deep. Then he climbs out an up onto a mountain 
# units high. Finally, he returns to sea level and ends his hike.

def countingValleys(n, s):
    valleys = 0
    level = 0
    for step in s:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        elif step == 'D':
            level -= 1
    return valleys

# a = [1,2,3,4,5]
# print(a[:2])




