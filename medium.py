def searchInSortedMatrix(matrix, target):
    for row in range(len(matrix)):
	    for col in range(len(matrix[0])):
	        if matrix[row][col] == target:
	            return [row, col]
	return [-1, -1]
