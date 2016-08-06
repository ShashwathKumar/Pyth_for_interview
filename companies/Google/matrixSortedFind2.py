import sys

def matrixFind(m,findNum):
	r = len(m)
	c = len(m[0])


	l = [row[c-1] for row in m]
	l = l[::-1]

	rowIndex = r
	#print l
	for num in l:
		rowIndex -= 1
		if findNum==num:
			return (rowIndex, c-1)
		elif findNum<num:
			continue
		else:
			rowIndex += 1
			break

	l = m[rowIndex][::-1]
	#print l
	colIndex = c
	for num in l:
		colIndex -= 1
		if findNum == num:
			return (rowIndex, colIndex)
		elif findNum < num:
			continue
		else:
			break

	return ()


def main(findNum):
	m = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],\
	    [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
	#print findNum,type(findNum)
	print matrixFind(m, findNum)


if __name__ == "__main__":
	main(int(sys.argv[1]))
