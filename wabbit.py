
garden = [
 [5, 7, 8, 6, 3],
 [0, 0, 7, 0, 4],
 [4, 6, 3, 4, 9],
 [3, 1, 0, 5, 8]]

def start(garden):
	rows = [len(garden) // 2, len(garden) // 2]
	cols = [len(garden[0]) // 2, len(garden[0]) // 2]

	if len(garden) % 2 != 0 and len(garden[0]) % 2 != 0:
		return rows[0], cols[0]

	if len(garden) % 2 == 0:
		rows[0] -= 1

	if len(garden[0]) % 2 == 0:
		cols[0] -= 1

	maxValue = 0
	startRow = None
	startCol = None

	for row in rows:
		for col in cols:
			if garden[row][col] > maxValue:
				maxValue = garden[row][col]
				startRow = row
				startCol = col

	return startRow, startCol

def nextRabbitSpace(garden, row, col):
	maxValue = 0
	nextRow = None
	nextCol = None

	for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
		currRow = row + r
		currCol = col + c

		if currRow >= 0 and currRow < len(garden) and \
			currCol >= 0 and currCol < len(garden[row]):

			if garden[currRow][currCol] > maxValue:
				maxValue = garden[currRow][currCol]
				nextRow = currRow
				nextCol = currCol

	carrots = garden[row][col]
	garden[row][col] = 0

	if maxValue > 0 and nextRow is not None and nextCol is not None:
		carrots += nextRabbitSpace(garden, nextRow, nextCol)

	return carrots

def hungryRabbit(garden):
	if len(garden) == 0 or len(garden[0]) == 0:
		return 0

	row, col = start(garden)
	return nextRabbitSpace(garden, row, col)

print(hungryRabbit(garden))
