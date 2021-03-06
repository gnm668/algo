def caesarCipher(str, key):
	alpha = list("abcdefghijklmnopqrstuvwxyz")
	str = list(str)
	newStr = []

	for i in range(len(str)):
		if str[i] == " ":
			newStr.append(str[i])
		else: 
			oldIdx = alpha.index(str[i])
			newIdx = (oldIdx + key) % 26
			newStr.append(alpha[newIdx])

	return "".join(newStr)		

# print(caesarCipher("who is that", 1))

def selectionSort(arr):
	for i in range(len(arr)):
		sIdx = i

		for j in range (i + 1, len(arr)):
			if arr[j] < arr[sIdx]:
				sIdx = j

		swap(sIdx, i, arr)			

	return arr

def swap(i, j, arr):
	arr[i], arr[j] = arr[j], arr[i]

# print(selectionSort([3,5,1]))

def insertionSort(arr):
	for i in range(len(arr)):
		j = i

		while j > 0 and arr[j] < arr[j - 1]:
			swap(j, j-1, arr)
			j -= 1

	return arr

# print(insertionSort([3,4,1]))

def threeLargest(arr):
	large = [None, None, None]

	for i in arr:
		update(large, i)

	return large

def update(largeArr, num):
	if largeArr[2] is None or largeArr[2] < num:
		shift(largeArr, num, 2)
	elif largeArr[1] is None or largeArr[1] < num:
		shift(largeArr, num, 1)
	elif largeArr[0] is None or largeArr[0] < num:
		shift(largeArr, num, 0)

def shift(largeArr, num, idx):
	for i in range(idx + 1):
		if i == idx:
			largeArr[i] = num
		else:
			largeArr[i] = largeArr[i + 1]

# print(threeLargest([4,2,1,5,6,4,3,3]))

def nthFib(num):
	lastTwo = [0, 1]
	counter = 3

	while counter <= num:
		temp = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = temp
		counter += 1

	return lastTwo[1] if num > 1 else lastTwo[0]

# print(nthFib(4))

# def twoSum(arr, tar):
# 	arr.sort()
# 	left = 0
# 	right = len(arr) - 1

# 	while left < right:
# 		currSum = arr[left] + arr[right]
# 		if currSum == tar:
# 			return [arr[left], arr[right]]
# 		elif currSum < tar:
# 			left += 1
# 		elif currSum > tar:
# 			right -= 1

# print(twoSum([4,3,2,1], 5))



def binarySearch(arr, tar):
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if arr[mid] == tar:
			return mid
		elif arr[mid] > tar:
			right = mid - 1
		elif arr[mid] < tar:
			left = mid + 1
		else:
			return -1

# print(binarySearch([1,2,3,4,5,6], 3))

def productSum(arr, multi = 1):
	sum = 0
	for el in arr:
		if type(el) is list:
			sum += productSum(el, multi + 1)
		else:
			sum += el
	return sum * multi

# print(productSum([1,2,[2,4]])) 

def elementCount(arr):
	count = {}

	for el in arr:
		if el in count:
			count[el] += 1
		else:
			count[el] = 1
	return count

# print(elementCount(['e', 'a', 'f', 'c', 'w', 'c']))


def anagrams(str1, str2):
	count = {}

	for char in str1:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1

	for char in str2:
		if char in count:
			count[char] -= 1
		else:
			count[char] = -1

	return all(value == 0 for value in count.values())

# print(anagrams("hello", "ello"))

# def twoSum(arr, tar):
# 	arr.sort()
# 	right = 0
# 	left = len(arr) - 1

# 	for el in arr:
# 		sum = arr[right] + arr[left]
# 		if sum == tar:
# 			return [arr[right], arr[left]]
# 		elif sum > tar:
# 			right -= 1
# 		elif sum < tar:
# 			left += 1

# def twoSum(arr, tar):
# 	store = {}
# 	for el in arr:
# 		otherNum = tar - el
# 		if otherNum in store:
# 			return [otherNum, el]
# 		else:
# 			store[el] = True

# print(twoSum([4,3,2,1], 5))

# def substrings(string):
# 	strArr = list(string)
# 	subs = []
	
# 	for i in range(len(strArr)):
# 		for j in range(i + 1, len(strArr)):
# 			sub = (strArr[i:j + 1])
# 			subs.append(sub)

# 	for i in range(len(subs)):
# 		subs[i] = ''.join(subs[i])
		
# 	return subs

# print(substrings('hello'))

# def revStr(str):
# 	newStr = []
# 	for i in range(len(str) - 1, -1, -1):
# 		newStr.append(str[i])
# 	return ''.join(newStr)

# print(revStr('hello'))

# def palindrome(strings):
# 	pals = []
# 	for str in strings:
# 		if str == revStr(str):
# 			pals.append(str)
# 	return pals

# def longestPalindromicSubstring(string):
# 	if len(string) == 1:
# 		return string
	
# 	subs = substrings(string)
# 	pals = palindrome(subs)
	
# 	if len(pals) > 0:
# 		return max(pals, key=len)
# 	else: 
# 		return	

# x = ['hello', 'hi', 'loo']
# print(max(x, key=len))

def longestPalindromicSubstring(string):
	currLongest = [0, 1]
	# will always be first string length of 1

	for i in range(1, len(string)):
		#exclusive end

		odd = getLongestPalidrome(string, i - 1, i + 1)
		#with i as center of palindrome

		even = getLongestPalidrome(string, i - 1, i)
		#with i and i -1 as center of even palidrome

		longest = max(odd, even, key = lambda x: x[1] - x[0])
		#grab longer palindrome between odd and even
		#review key = lambda python

		currLongest = max(longest, currLongest, key = lambda x: x[1] - x[0])
		#grab longer palindrome between currLongest and longest

	return string[currLongest[0]: currLongest[1]]

def getLongestPalidrome(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		#until one of the indices doesn't work

		if string[leftIdx] != string[rightIdx]:
			#break if not pal

			break

		leftIdx -= 1
		rightIdx += 1
		#increment
	
	return [leftIdx + 1, rightIdx]


# print(longestPalindromicSubstring('abaxxyyzzyyxxb'))

# a = 'hello'
# a = sorted(a)
# a = ''.join(a)
# print(a)

# a = ['hi', 'look']
# def foo(words):
# 	return max(words[0], words[1], key= lambda a: len(a))

# a = foo(a)
# print(a) 

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


# print('HELLO'.lower())

# a = {'a': 1, 'b': 2}

# print(a[1])
# print('a' in a)

# b = [1,2,3,4]
# print(b[4])

# board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

# a = 'hello'
# print('h' in a)

# def bubbleSort(arr):
# 	isSort = False
# 	while not isSort:
# 		isSort = True
# 		for i in range(len(arr) - 1):
# 			if arr[i] > arr[i + 1]:
# 				swap(i, i + 1, arr)
# 				isSort = False
# 	return arr

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]
	

# def twoSum(arr, tar):
	# arr.sort()
	# left = 0
	# right = len(arr) - 1

	# while left < right:
	# 	currSum = arr[left] + arr[right]
	# 	if currSum == tar:
	# 		return [arr[left], arr[right]]
	# 	elif currSum > tar:
	# 		right -= 1
	# 	else:
	# 		left += 1
	# return []


# t = 12

# def twoSum(arr, tar):
# 	diffs = {}   
# 	for el in arr: 
# 		if tar - el in diffs:
# 			return [diffs[tar - el], el] 
# 		diffs[el] = el
# 	return []

# a = [5, 2, 6, 1, 7]

# def quickSort(arr):
# 	# print(arr)
# 	if len(arr) <= 1:
# 		return arr

# 	pivot = arr[0]
# 	left = [x for x in arr[1:] if x < pivot]
# 	right = [x for x in arr[1:] if x >= pivot]

# 	return quickSort(left) + [pivot] + quickSort(right)


# def quickSort2(array):
# 	if len(array) <= 1:
# 		return array

# 	pivot = array[0]
# 	left = [x for x in array if x < pivot]
# 	middle = [x for x in array if x == pivot]
# 	right = [x for x in array if x > pivot]
# 	return quickSort2(left) + middle + quickSort2(right)


# print(quickSort(a))
# print(a)

a = [-9, 8, -10, 4, 10, 8, -2, -5, -10, 2, 5, 3, -7, -7, 2, 3, -6, 9]

# print(a)

# print(quickSort2(a))
# print(quickSort(a))

# lucs number sequence start with 2, 1

# def lucasNumber(num, memo = {}):
# 	if num in memo: return memo[num]
# 	if num == 0: return 2
# 	if num == 1: return 1
	
# 	memo[num] = lucasNumber(num - 1, memo) + lucasNumber(num - 2, memo)
# 	return memo[num]

# print(lucasNumber(1000))

# def lucasNum(num):
# 	table = [2, 1]

# 	for i in range(2, num):
# 		table.append(table[i - 1] + table[i - 2])

# 	print(table)
# 	return table[num - 1]

# print(lucasNum(50))

# def bubbleSort(arr):
# 	sort = False
# 	while not sort:
# 		sort = True
# 		for i in range(1, len(arr)):
# 			if arr[i - 1] > arr[i]:
# 				swap(i, i - 1, arr)
# 				sort = False
# 	return arr

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]


# print(bubbleSort(test))

# test = [5,4,3,2,1]

# def quickSort(arr):
# 	if len(arr) <= 1:
# 		return arr

# 	pivot = arr[0]

# 	left = [x for x in arr[1:] if x < pivot]
# 	right = [x for x in arr[1:] if x >= pivot]

# 	return quickSort(left) + [pivot] + quickSort(right)

# print(quickSort(test))

# def twoSum(arr, tar):
# 	diff = {}
	
# 	for el in arr:
# 		if tar - el in diff:
# 			return [el, diff[tar - el]]
# 		diff[el] = el
# 	return []

nums = [1,2,3,6]

# print(twoSum(nums, 9))

# def twoSum(arr, tar):
# 	arr.sort()
# 	left = 0
# 	right = len(arr) - 1

# 	while left < right:
# 		if arr[left] + arr[right] == tar:
# 			return [arr[left], arr[right]]
# 		elif arr[left] + arr[right] > tar:
# 			right -= 1
# 		elif arr[left] + arr[right] < tar:
# 			left += 1
# 	return []

# print(twoSum(nums, 9))

# def lucasNum(num, memo = {0: 2, 1: 1}):
# 	if num in memo: return memo[num]

# 	memo[num] = lucasNum(num - 1, memo) + lucasNum(num - 2, memo)
# 	return memo[num]

# def lucasNum(num):
# 	table = [2, 1]
# 	if num == 0: return table[0]

# 	for i in range(1, num):
# 		temp = table[1]
# 		table[1] = table[1] + table[0]
# 		table[0] = temp
# 	return table[1]
		

# print(lucasNum(3))

# def minChange(coins, amount, memo = {}):
# 	if amount in memo: return memo[amount]
# 	if amount == 0: return 0
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# print(minChange([1,5,10,25], 800))

# def bubbleSort(li):
# 	isSort = False
# 	while not isSort:
# 		isSort = True
# 		for i in range(1, len(li)):
# 			if li[i - 1] > li[i]:
# 				swap(i, i - 1, li)
# 				isSort = False
# 	return li

# def swap(i, j, li):
# 	li[i], li[j] = li[j], li[i]

# testLi = [5, 4, 3, 2, 2, 3, 4, 5, 6, -10, -10, -1, -3]

# def quickSort(li):
# 	if len(li) <= 1:
# 		return li

# 	pivot = li.pop(0)
# 	left = [el for el in li if el < pivot]
# 	right = [el for el in li if el >= pivot]

# 	return quickSort(left) + [pivot] + quickSort(right)

# def lucasNum(num, memo = {0: 2, 1: 1}):
# 	if num in memo: return memo[num]

# 	memo[num] = lucasNum(num - 1) + lucasNum(num - 2)
# 	return memo[num]

# def lucasNum(num):
# 	table = [2, 1]

# 	if num == 0: return table[0]

# 	for i in range(1, num):
# 		temp = table[1]
# 		table[1] = table[0] + table[1]
# 		table[0] = temp

# 	return table[1]

# def twoSum(li, tar):
# 	li.sort()
# 	left = 0
# 	right = len(li) - 1

# 	while left < right:
# 		if li[left] + li[right] == tar:
# 			return [li[left], li[right]]
# 		elif li[left] + li[right] > tar:
# 			right -= 1
# 		elif li[left] + li[right] < tar:
# 			left += 1
# 	return []

# def twoSum(li, tar):
# 	diffs = {}

# 	for el in li:
# 		if el in diffs:
# 			return [diffs[el], el]
# 		diffs[tar - el] = el
# 	return []

# print(twoSum([5,4,3,2,1,6,5,3,1,5,7,86,4,1,5,7,75,4,3], 161))

# def minChange(coins, amount, memo = {}):
# 	if amount in memo: return memo[amount]
# 	if amount == 0: return 0 
# 	numCoins = []

# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount  - coin, memo) + 1)
	
# 	memo[amount] = min(numCoins)
# 	return memo[amount]


# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0

# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remainder = amt - qty * coin
# 				attempt = table[remainder] + qty
# 				if attempt < table[amt]: table[amt] = attempt 
# 				qty += 1
# 	return table[-1]

# print(minChange([1,5,10,25], 800))

# go through coins 
# go through amts in table [1,2,3...amount] 
# check remainder of amt - (qty * coin) 
# check table for cheapest way to find remainder

# def quickSort(arr):
# 	if len(arr) <= 1: return arr
# 	pivot = arr.pop(0)

# 	left = [el for el in arr if el < pivot]
# 	right = [el for el in arr if el >= pivot]
# 	return quickSort(left) + [pivot] + quickSort(right)


# def bubbleSort(arr):
# 	isSort = False
# 	while not isSort:
# 		isSort = True
# 		for i in range(1, len(arr)):
# 			if arr[i - 1] > arr[i]:
# 				swap(i, i - 1, arr)
# 				isSort = False
# 	return arr

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]

# a = [3,3,2,2,1,5,6,5,32,23,4,5,2,1,3]

# print(bubbleSort(a))
			
# def lucasNumber(num, memo = {0: 2, 1: 1}):
# 	if num in memo: return memo[num]

# 	memo[num] = lucasNumber(num - 1) + lucasNumber(num - 2)
# 	return memo[num]

# def lucasNum(num):
# 	table = [2,1]

# 	if num == 0: return table[0]

# 	for i in range(num):
# 		temp = table[1]
# 		table[1] = table[1] + table[0]
# 		table[0] = temp
	
# 	return table[0]

# print(lucasNum(40))

# def twoSum(nums, tar):
# 	diffs = {}

# 	for num in nums:
# 		if num in diffs:
# 			return [diffs[num], num]
# 		diffs[tar - num] = num
	
# 	return []



# def twoSum(nums, tar):
# 	nums.sort()
# 	left = 0 
# 	right = len(nums) - 1

# 	while left < right:
# 		if nums[left] + nums[right] == tar:
# 			return [nums[left], nums[right]]
# 		elif nums[left] + nums[right] > tar:
# 			right -= 1
# 		else:
# 			left += 1
# 	return []

# print(twoSum([5,4,2,1], 9))

# def quickSort(li):
# 	if len(li) == 0: return li

# 	pivot = li.pop()
# 	left = [el for el in li if el < pivot]
# 	right = [el for el in li if el >= pivot]

# 	return quickSort(left) + [pivot] + quickSort(right)

# def minChange(coins, amount, memo = {}):
# 	if amount == 0: return 0
# 	numCoins = []

# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
	
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# print(minChange([1,2,5], 10))

# def bubbleSort(li):
# 	isSort = False
# 	while not isSort:
# 		isSort = True
# 		for i in range(1, len(li)):
# 			if li[i - 1] > li[i]:
# 				swap(i, i - 1, li)
# 				isSort = False
# 	return li

# def swap(i, j, arr):
# 	arr[i], arr[j] = arr[j], arr[i]

# test = [4,3,2,1]

# def quickSort(li):
# 	if len(li) == 0: return li
# 	pivot = li.pop()
# 	left = [el for el in li if el < pivot]
# 	right = [el for el in li if el >= pivot]
# 	return quickSort(left) + [pivot] + quickSort(right)

# print(quickSort(test))


# def minChange(coins, amount, memo = {}):
# 	if amount == 0: return 0 
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
	
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0

# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while coin * qty <= amt:
# 				remainder = amt - qty * coin
# 				attempt = table[remainder] + qty
# 				if attempt < table[amt]: table[amt] = attempt
# 				qty += 1
# 	return table[-1]

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0

# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remainder = amt - qty * coin
# 				attempt = table[remainder] + qty
# 				if attempt < table[amt]: table[amt] = attempt
# 				qty += 1
# 	return table[-1]



# def minChange(coins, amount, memo = {}):
# 	if amount == 0: return 0
# 	numCoins = []

# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0

# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remainder = amt - qty * coin 
# 				attempt = table[remainder] + qty
# 				if attempt < table[amt]: table[amt] = attempt
# 				qty += 1
# 	return table[-1]

# def minChange(coins, amount, memo = {}):
# 	if amount == 0: return 0 
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount: 
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# def quickSort(li):
# 	if len(li) == 0: return li
# 	pivot = li.pop()
# 	left = [el for el in li if el < pivot]
# 	right = [el for el in li if el >= pivot]
# 	return quickSort(left) + [pivot] + quickSort(right)

# print(quickSort([5,4,3,2,1]))

# def bubbleSort(li):
# 	isSort = False
# 	while not isSort:
# 		isSort = True
# 		for i in range(1, len(li)):
# 			if li[i - 1] > li[i]:
# 				swap(i, i - 1, li)
# 				isSort = False
# 	return li

# print(bubbleSort([5,4,3,2,1]))

# def minChange(coins, amount, memo = {}):
# 	if amount == 0: return 0
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0
# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remainder = amt - (qty * coin)
# 				attempt = table[remainder] + qty
# 				if attempt < table[amt]: table[amt] = attempt
# 				qty += 1
# 	return table[-1]
		
# print(minChange([1, 2, 5], 10))

# def quickSort(li):
# 	if len(li) == 0: return li
# 	pivot = li.pop()
# 	left = [el for el in li if el <= pivot]
# 	right = [el for el in li if el > pivot]
# 	return quickSort(left) + [pivot] + quickSort(right)

# print(quickSort([5,4,3,2,1]))

# def minChange(coins, amount, memo = {0: 0}):
# 	if amount in memo: return memo[amount]
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0
# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remain = amt - (qty * coin)
# 				attempt = table[remain] + qty
# 				if table[amt] > attempt: table[amt] = attempt
# 				qty += 1
# 	return table[-1]
# print(minChange([1, 2, 5], 10))

# def threeSum(li, tar):
# 	li.sort()
# 	res = []
# 	for i in range(len(li)):
# 		left = i + 1
# 		right = len(li) - 1
# 		while left < right:
# 			currSum = li[i] + li[left] + li[right]
# 			if currSum == tar:
# 				res.append([li[i], li[left], li[right]])
# 				right -= 1
# 				left += 1
# 			elif currSum > tar:
# 				right -= 1
# 			elif currSum < tar:
# 				left += 1
# 	return res

# print(threeSum([6,2,1,3,5,6,0], 8))

# def smallestDiff(li1, li2):
# 	li1.sort()
# 	li2.sort()
# 	idx1, idx2 = 0, 0 
# 	curr, diff = float('inf'), float('inf')
# 	pair = []
# 	while idx1 < len(li1) and idx2 < len(li2):
# 		num1, num2 = li1[idx1], li2[idx2]
# 		if num1 < num2:
# 			curr = num2 - num1
# 			idx1 += 1
# 		elif num1 > num2:
# 			curr = num1 - num2
# 			idx2 += 1
# 		else:
# 			return [num1, num2]
# 		if curr < diff:
# 			diff = curr
# 			pair = [num1, num2]
# 	return pair

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# def moveElementToEnd(li, toMove):
# 	i = 0
# 	j = len(li) - 1
# 	while i < j:
# 		while i < j and li[j] == toMove:
# 			j -= 1
# 		if li[i] == toMove:
# 			li[i], li[j] = li[j], li[i]
# 		i += 1
# 	return li

# print(moveElementToEnd([2,1,2,2,2,4,3,2], 2))


# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []

#     def addChild(self, name):
#         self.children.append(Node(name))
#         return self

#     def bfs(self, array):
# 		queue = [self]
# 		while len(queue):
# 			curr = queue.pop(0)
# 			array.append(curr.name)
# 			for child in curr.children:
# 				queue.append(child)
# 		return array

# tree = Node('A')
# tree.addChild('B')
# tree.addChild('C')
# tree.children[0].addChild('D')
# tree.children[0].addChild('E')
# tree.children[1].addChild('F')

# print(tree.bfs([]))

# def moveElToEnd(li, toMove):
# 	i = 0
# 	j = len(li) - 1
# 	while i < j:
# 		while i < j and li[j] == toMove:
# 			j -= 1
# 		if li[i] == toMove:
# 			li[i], li[j] = li[j], li[i]
# 		i += 1
# 	return li

# print(moveElToEnd([2,1,2,2,2,4,3,2], 2))

# def moveEltoEnd(li, toMove):
# 	i = 0 
# 	j = len(li) - 1 # i = 1, j = 5
# 	while i < j:
# 		while i < j and li[j] == toMove:
# 			j -= 1
# 		if li[i] == toMove
# 			li[i], li[j] = li[j], li[i]
# 		i += 1
# 	return li

# def moveElToEnd(li, toMove):
# 	i = 0
# 	j = len(li) - 1
# 	while i < j:
# 		while i < j and li[j] == toMove:
# 			j -=1
# 		if li[i] == toMove:
# 			li[i], li[j] = li[j], li[i]
# 		i += 1
# 	return li

# print(moveElToEnd([2,1,2,2,2,4,3,2], 2))

# class Node:
# 	def __init__(self, name):
# 		self.name = name
# 		self.children = []

# 	def addChild(self, name):
# 		self.children.append(Node(name))
# 		return self
	
# 	def bfs(self, array):
# 		queue = [self]
# 		while len(queue):
# 			curr = queue.pop(0)
# 			array.append(curr.name)
# 			for child in curr.children:
# 				queue.append(child)
# 		return array

# tree = Node('A')
# tree.addChild('B')
# tree.addChild('C')
# tree.children[0].addChild('D')
# tree.children[0].addChild('E')
# tree.children[1].addChild('F')

# print(tree.bfs([]))

# def threeSum(li, tar):
# 	li.sort()
# 	res = []
# 	for i in range(len(li)):
# 		left = i + 1
# 		right = len(li) - 1
# 		while left < right:
# 			currSum = li[i] + li[left] + li[right]
# 			if currSum == tar:
# 				res.append([li[i], li[left], li[right]])
# 				left += 1
# 				right -= 1
# 			elif currSum > tar:
# 				right -= 1
# 			else: 
# 				left += 1
# 	return res 

# print(threeSum([6,2,1,3,5,6,0], 8))

# def smallestDiff(li1, li2):
# 	li1.sort()
# 	li2.sort()
# 	idx1, idx2 = 0, 0
# 	diff, curr = float('inf'), float('inf')
# 	pair = []
# 	while idx1 < len(li1) and idx2 < len(li2):
# 		num1, num2 = li1[idx1], li2[idx2]
# 		if num1 > num2:
# 			curr = num1 - num2
# 			idx2 += 1
# 		elif num1 < num2:
# 			curr = num2 - num1
# 			idx1 += 1
# 		else:
# 			return [num1, num2]
# 		if curr < diff:
# 			diff = curr
# 			pair = [num1, num2]
# 	return pair

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1) 
# 	table[0] = 0
# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remain = amt - (qty * coin)
# 				attempt = table[remain] + qty
# 				if attempt < table[amt]: table[amt] = attempt
# 				qty += 1
# 	return table[-1]



# def minChange(coins, amount, memo = {0:0}):
# 	if amount in memo: return memo[amount]
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin, memo) + 1)
# 	memo[amount] = min(numCoins)
# 	return memo[amount]

# print(minChange([1,2,5], 26))

# def minChange(coins, amount):
# 	if amount == 0: return 0
# 	numCoins = []
# 	for coin in coins:
# 		if coin <= amount:
# 			numCoins.append(minChange(coins, amount - coin) + 1)
# 	return min(numCoins)

# def moveElToEnd(li, toMove):
# 	i = 0
# 	j = len(li) - 1
# 	while i < j:
# 		while i < j and li[j] == toMove:
# 			j -= 1
# 		if li[i] == toMove:
# 			li[i], li[j] = li[j], li[i]
# 		i += 1
# 	return li
	
# print(moveElToEnd([2,1,2,2,2,4,3,2], 2))

# def minChange(coins, amount):
# 	table = [float('inf')] * (amount + 1)
# 	table[0] = 0
# 	for coin in coins:
# 		for amt in range(len(table)):
# 			qty = 0
# 			while qty * coin <= amt:
# 				remain = amt - (coin * qty)
# 				attempt = table[remain] + qty
# 				if attempt < table[amt]: table[amt] = attempt
# 				qty += 1
# 	return table[-1]

# print(minChange([1,2,5], 26))

# def threeSum(li, tar):
# 	li.sort()
# 	res = []
# 	for i in range(len(li)):
# 		left = i + 1
# 		right = len(li) - 1
# 		while left < right:
# 			currSum = li[i] + li[left] + li[right]
# 			if currSum == tar:
# 				res.append([li[i], li[left], li[right]])
# 				right -= 1
# 				left += 1
# 			elif currSum > tar:
# 				right -= 1
# 			else: 
# 				left += 1
# 	return res

# print(threeSum([6,2,1,3,5,6,0], 8))

# def smallestDiff(li1, li2):
# 	li1.sort()
# 	li2.sort()
# 	idx1, idx2 = 0, 0 
# 	diff, curr = float('inf'), float('inf')
# 	pair = []
# 	while idx1 < len(li1) and idx2 < len(li2):
# 		num1, num2 = li1[idx1], li2[idx2]
# 		if num1 < num2:
# 			curr = num2 - num1
# 			idx1 += 1
# 		elif num1 > num2:
# 			curr = num1 - num2
# 			idx2 += 1
# 		else:
# 			return [num1, num2]
# 		if curr < diff:
# 			diff = curr
# 			pair = [num1, num2]
# 	return pair

# print(smallestDiff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
