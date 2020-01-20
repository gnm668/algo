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

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value):
		node = self.head
		while self.head is not None and node.value != value
			node = node.next
		return node is not None   

    def remove(self, node):
		if node = self.head:
			self.head = self.head.next
		if node = self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

	def removeNodeBindings(node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.next = None
		node.prev = None

    def removeNodesWithValue(self, value):
		# test my version
		# node = self.head
		# while node is not None:
		# 	if node.value == value:
		# 		temp = node
		# 	node = node.next
		# 	self.remove(temp)
		
		node = self.head
		while node is not None:
			temp = node
			node = node.next
			if temp.value == value:
				self.remove(temp)		

	def insertNodeBefore(self, node, nodeToInsert):
		if self.head == nodeToInsert and self.tail == nodeToInsert:
			return
		self.remove(nodeToInsert)
		nodeToInsert.next = node
		nodeToInsert.prev = node.prev
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert	
		
    def insertAfter(self, node, nodeToInsert):
		if self.head = nodeToInsert and self.tail = nodeToInsert:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)

    def setTail(self, node):
		if self.head is None:
			self.setHead(node)
		self.insertAfter(self.tail, node)	
