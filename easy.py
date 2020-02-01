def twoNumberSum(array, targetSum):
    differences = {}

    for el in array:
        difference = targetSum - el
        if el in differences:
            return [el, difference]
        else:
            differences[difference] = True
    return []

print(twoNumberSum([1,2,3,9], 5))
