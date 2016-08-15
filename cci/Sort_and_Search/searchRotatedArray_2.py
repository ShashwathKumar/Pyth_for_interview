def search(a,e):
	minv = 0
	maxv = len(a)-1
	mid  = (minv + maxv)/2
	print a, mid, minv, maxv
	if not a:
		return None
	elif a[mid]==e:
		return mid
    #left is ordered
	elif a[minv] < a[mid]:
		print 'a[minv] < a[mid]'
		if a[minv] <= e < a[mid]:
			return search(a[:mid], e)
		else:
			return mid+1+search(a[mid+1:], e)
	#right is ordered
	elif a[maxv] > a[mid]:
		print 'a[maxv] > a[mid]'
		if a[mid] < e <= a[maxv]:
			return mid+1+search(a[mid+1:], e)
		else:
			return search(a[:mid], e)
    #left == mid (repeats)
	elif a[minv] == a[mid]:
		#right is diff -- search
		print 'a[minv]==a[mid]'
		if a[maxv] != a[mid]:
			return mid+1+search(a[mid+1:], e)
		#search both halves
		else:
			leftres = search(a[:mid], e)
			if leftres is not None:
			    return leftres
			else:
				rightres = search(a[mid+1:], e)
				rightres = mid+1+rightres if rightres is not None else None
				return rightres

def main():
	a = [6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5]
	e = 8
	print search(a, e)

if __name__ == "__main__":
	main()