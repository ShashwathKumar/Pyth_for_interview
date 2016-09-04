def magic(l):
	low  = 0
	high = len(l)-1

	while low<=high:
		mid = (low+high)/2
		if l[mid]==mid:
			return mid
		elif mid<l[mid]:
			high = mid-1
		else:
			low  = mid+1
	return None

def main():
	l = [0, 1, 2, 4, 6, 7, 8, 20]
	print magic(l)

if __name__ == "__main__":
	main()


