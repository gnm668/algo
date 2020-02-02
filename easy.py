def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum > targetSum:
            right -= 1
        elif currentSum < targetSum:
            left += 1
        else:
            return [array[left], array[right]]
    return []
    # differences = {}

    # for el in array:
    #     difference = targetSum - el
    #     if el in differences:
    #         return [el, difference]
    #     else:
    #         differences[difference] = True
    # return []

# print(twoNumberSum([1,2,3,9], 5))


# def getNthFib(n):
#     if n == 1:
# 	    return 0
#     if n == 2:
# 	    return 1
# 	return getNthFib(n - 1) + getNthFib(n - 2)
# O(2^n) time
# O(n) space

def getNthFib(n, memo = {1: 0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = getNthFib(n - 1) + getNthFib(n - 2)
    return memo[n]
# O(n) time
# O(n) space
# print(getNthFib(6))


# def getNthFib(n):
# 	lastTwo = [0, 1]
# 	if n == 1:
# 		return lastTwo[0]
# 	if n == 2:
# 		return lastTwo[1]
# 	for i in range(2, n):
# 		nextNum = lastTwo[0] + lastTwo[1]
# 		lastTwo[0] = lastTwo[1]
# 		lastTwo[1] = nextNum
# 	return lastTwo[1]
# O(n) time
# O(1) space

def productSum(array, multi=1):
    sum = 0
    for el in array:
        if type(el) is list:
            sum += productSum(el, multi + 1)
        else:
            sum += el
    return sum * multi

# print(productSum(a))

def threeLargest(array):
    largest = [None, None, None]
    for num in array:
        update(largest, num)
    return largest

def update(largest, num):
    if largest[2] is None or num > largest[2]:
        shift(largest, num, 2)
    elif largest[1] is None or num > largest[1]:
        shift(largest, num, 1)
    elif largest[0] is None or num > largest[0]:
        shift(largest, num, 1)

def shift(largest, num, idx):
    for i in range(idx + 1):
        if i == idx:
            largest[i] = num
        else:
            largest[i] = largest[i + 1]

# a = [10,5,9,10,12]

# print(threeLargest(a))


def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                isSorted = False
    return array


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]


def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
    return array


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(array, smallestIdx, currentIdx)
        currentIdx += 1
    return array

a = [5,4,3,2,1]

# print(selectionSort(a))

def palidromeCheck(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# print(palidromeCheck('elle'))


def caesarCipherEncryptor(string, key):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    stringList = list(string)
    newStr = []

    for char in stringList:
        if char in alpha:
            oldIdx = alpha.index(char)
            newIdx = (oldIdx + key) % 26
            newStr.append(alpha[newIdx])
        else:
            newStr.append(char)
    
    newStr = "".join(newStr)
    return newStr

print(caesarCipherEncryptor('where are you', 25))
