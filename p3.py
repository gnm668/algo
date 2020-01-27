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


def groupAnagrams(words):	
	groups = {} #O(WN) Space
	
	for word in words:  #O(N) Time
		sortedWord = "".join(sorted(word)) #O(Wlog(W) Time
		if sortedWord in groups:
			groups[sortedWord].append(word)
		else:
			groups[sortedWord] = [word]
			
	return groups.values() 
