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

print(twoNumberSum([1,2,3,9], 5))

