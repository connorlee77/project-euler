dimen = 21

def initGrid():
	arr = []
	for x in range(dimen):
		arr.append([])
		for y in range(dimen):
			if x == dimen - 1 or y == dimen - 1:
				arr[x].append(1)
			else: 
				arr[x].append(0)
	return arr


def countTracks():
	mat = initGrid()

	for x in range(dimen - 1)[::-1]:
		for y in range(dimen - 1)[::-1]:
			mat[x][y] = mat[x + 1][y] + mat[x][y + 1]

	return mat[0][0]

print countTracks()