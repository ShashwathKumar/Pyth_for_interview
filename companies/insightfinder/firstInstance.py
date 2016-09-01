#give first instance of a given number in a list
from math import ceil, floor

def firstInstance(l, num):
	low = 0
	high = len(l)-1

	while low<=high:
		mid = int(ceil((low+high)/2))
		if num>l[mid]:
			low = mid+1
		else:
			high = mid-1
	return mid

def firstInstance2(l, num):
	low = 0
	high = len(l)-1

	while low<high:         #1
		mid = (low+high)/2  #2
		if num>l[mid]:
			low = mid+1
		else:
			high = mid      #3
	else:
		if l[low]==num:     #*
			return low

def lastInstance(l, num):
	low = 0
	high = len(l)-1

	while low<high:
		mid = (low+high)/2
		if num<l[mid]:
			high = mid-1
		else:
			low = mid
	else:
		if l[high]==num:
			return high


	# low = 0
	# high = len(l)-1

	# while not low>high:
	# 	mid = int(ceil((low+high)/2))
	# 	if num<l[mid]:
	# 		high = mid-1
	# 	else:
	# 		low = mid+1
	# return mid

def main():
	l = [1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 6, 7]
	print firstInstance(l, 4)
	print firstInstance2(l, 4)
	print lastInstance(l,4)

if __name__=="__main__":
	main()