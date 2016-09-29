#That extra mem is used in the first index of each row.
#Can think of a way to eliminate that

def subsetSum(arr, sumx):
	tmp = [[False for j in xrange(sumx+1)] for n in arr]

	for i, n in enumerate(arr):
		for j in xrange(1,sumx+1):
			if j==n:
				tmp[i][j]=True
			elif i>0 and j>=n and (tmp[i-1][j]==True or tmp[i-1][j-n]==True):
				tmp[i][j]=True

	return tmp[len(arr)-1][sumx-1]

def main():
	arr  = [1, 3, 5, 4, 7]
	sumx = 11
	print subsetSum(arr, sumx)

if __name__=="__main__":
	main()