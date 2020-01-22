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

def twoSum(arr, tar):
	arr.sort()
	left = 0
	right = len(arr) - 1

	while left < right:
		currSum = arr[left] + arr[right]
		if currSum == tar:
			return [arr[left], arr[right]]
		elif currSum < tar:
			left += 1
		elif currSum > tar:
			right -= 1

# print(twoSum([4,3,2,1], 5))



x = sum([x*x for x in [1,2,3]])
print(x)

print(int(2/2))

