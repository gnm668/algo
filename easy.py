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