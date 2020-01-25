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







































