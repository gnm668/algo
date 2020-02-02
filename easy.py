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

a = [10,5,9,10,12]

print(threeLargest(a))
