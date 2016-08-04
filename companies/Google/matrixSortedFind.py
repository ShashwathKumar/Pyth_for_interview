from math import floor

def matrixFind(m, findNum):
	r = len(m)
	c = len(m[0])
	ratio = c/r

	diagonalList = []
	rIndex = 0

	while True:
		cIndex = int(floor(ratio*rIndex))
		if rIndex >= r or cIndex >= c:
			break
		diagonalList.append((m[rIndex][cIndex],rIndex,cIndex))
		rIndex += 1

	print diagonalList
	midTuples = binSearchDiag(diagonalList, findNum)
	print "midTuples: ",midTuples
	if len(midTuples)==1:
		mid = midTuples[0]
		print (diagonalList[mid][1],diagonalList[mid][2])
	else:
		res = ()
		if midTuples[1]>len(diagonalList)-1:
		    res = binSearch4((diagonalList[midTuples[0]][1], None),\
	                         (diagonalList[midTuples[0]][2], None), m, findNum)
		elif midTuples[0]<0:
			res = binSearch4((None, diagonalList[midTuples[1]][1]),\
	        			     (None, diagonalList[midTuples[1]][2]), m, findNum)
		else:
			res = binSearch4((diagonalList[midTuples[0]][1], diagonalList[midTuples[1]][1]),\
	        			     (diagonalList[midTuples[0]][2], diagonalList[midTuples[1]][2]), m, findNum)
		print res

def binSearch4(r, c, m, findNum):
    print "binSearch4",r,c

    for rowIndex in r:
		if rowIndex == None:
			continue
		res = binSearch(m[rowIndex], findNum)
		if res != -1:
			return (rowIndex, res)

    for colIndex in c:
		if colInex == None:
			continue
		col = [l[colIndex] for l in m]
		res = binSearch(col, findNum)
		if res != -1:
			return (res, colIndex)

    return ()

def binSearch(l, findNum):
	min = 0
	max = len(l)-1
	print l

	while not min>max:
		mid = (min+max)/2
		print l[mid], min, max, mid
		if l[mid]==findNum:
			return mid
		elif findNum < l[mid]:
			max = mid-1
		else:
			min = mid+1

	#search failed
	return -1

def binSearchDiag(diagonalList, findNum):
	length = len(diagonalList)
	min = 0
	max = length-1
	found = 0

	while min<=max:
		mid = (min+max)/2

		if diagonalList[mid][0] == findNum:
			found = 1
			break
			print "found ", findNum
		elif findNum<diagonalList[mid][0]:
			max = mid-1
			print str(findNum)+"<"+str(diagonalList[mid][0])
		elif findNum>diagonalList[mid][0]:
			min = mid+1
			print str(findNum)+">"+str(diagonalList[mid][0])

	if(found==1):
		return (mid,)
	else:
		if diagonalList[mid]<findNum:
			return (mid, mid+1)
		else:
			return (mid-1, mid)

def main():
	m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
	findNum = 12
	matrixFind(m, findNum)

if __name__ == "__main__":
	main() 	