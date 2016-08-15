def search(a, e):
	if not a:
		return None
	minv=0
	maxv=len(a)-1
	mid = (minv+maxv)/2
	if a[mid]==e:
		return mid
	#search right array -- < half rotated
	elif a[mid] < e < a[maxv]:
		return mid+1+search(a[mid+1:],e)
	#search left  array -- < half rotated
	elif e < a[mid] < a[minv]:
		return search(a[:mid] , e)
	#search left  array -- > half rotated
	elif a[mid] > e > a[minv]:
		return search(a[:mid] , e)
	#search right array -- > half rotated
	elif e < a[maxv] < a[mid]:
		return mid+1+search(a[mid+1:],e)
	else:
		leftres  = search(a[:mid]  , e)  #search left  array
		rightres = search(a[mid+1:], e)  #search right array
		rightres = mid+1+rightres if rightres is not None else rightres
		return leftres if leftres else rightres

def main():
	a = [6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5]
	e = 2
	print search(a, e)

if __name__ == "__main__":
	main()