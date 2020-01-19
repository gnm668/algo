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

#time O(2^n) without meomoize
#space O(n) -- recursion call stack without memoize
#time O(n) with memoize
#space O(n) with memoize
#if using memoize with base cases, can store base cases in memo hash

def getNthFib(n):
	lastTwo = [0, 1]
	counter = 3

	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1

	return lastTwo[1] if n > 1 else lastTwo[0]

print(getNthFib(50))
