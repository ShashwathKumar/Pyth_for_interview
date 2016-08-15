def findSizeWithE(l,e, assumedSize):
	if e<=l[assumedSize]:
		return assumedSize
	else:
		return findSizeWithE(l,e, assumedSize*2)

def search_rec(l, e, minv, maxv):
	if minv>maxv:
		return None
	mid = (minv+maxv)/2
	if e==l[mid]:
		return mid
	elif l[mid]<e:
		minv = mid+1
		return search_rec(l, e, minv, maxv)
	else:
		maxv = mid-1
		return search_rec(l, e, minv, maxv)

def search(l,e):
	assumedSize = 2
	try:
		emax = findSizeWithE(l,e, assumedSize)
	except IndexError:
		eindex = None
		return eindex
	minv = emax/2
	maxv = emax
	eindex = search_rec(l,e,minv,maxv)
	return eindex # I could have put it in previous statement itself. Kept here for clarity

def main():
	l = [1, 2, 3, 6, 8, 10, 12, 14, 17]
	e = 8
	eindex = search(l,e)
	print eindex if eindex else 'Not Found'

if __name__ == "__main__":
	main()