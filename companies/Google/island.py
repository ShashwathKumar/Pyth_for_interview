def island(m):
	s = set()
	r = len(m)
	c = len(m[0])
	cnt = 0

	for i, row in enumerate(m):
		for j, n in enumerate(row):
			if m[i][j] and (i,j) not in s:
				s.add((i,j))
				s.union(island_rec(m,i,j,r,c,s))
				#print s
				cnt += 1
	return cnt

def island_rec(m,i,j,r,c,s):

	if i>0 and m[i-1][j] and (i-1,j) not in s:
		s.add((i-1,j))
		s.union(island_rec(m,i-1,j,r,c,s))
	if i<r-1 and m[i+1][j] and (i+1,j) not in s:
		s.add((i+1,j))
		s.union(island_rec(m,i+1,j,r,c,s))
	if j>0 and m[i][j-1] and (i,j-1) not in s:
		s.add((i,j-1))
		s.union(island_rec(m,i,j-1,r,c,s))
	if j<c-1 and m[i][j+1] and (i,j+1) not in s:
		s.add((i,j+1))
		s.union(island_rec(m,i,j+1,r,c,s))

	return s

def main():
	m = [[0, 0, 1, 1],
	     [0, 0, 1, 0],
	     [1, 1, 1, 0],
	     [0, 1, 0, 1]]
	print island(m)

if __name__ == "__main__":
	main()