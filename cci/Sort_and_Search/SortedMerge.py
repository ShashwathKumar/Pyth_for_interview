def sortedMerge(a, b, aend):
	lengtha = len(a)
	lengthb = len(b)
	i = aend #assuming aend to be the last valid index in a
	j = lengthb-1
	k = lengtha-1

	while i>=0 and j>=0:
		a[k]=max(a[i],b[j])
		if a[k]==a[i]:
			i-=1
		else:
			j-=1
		k-=1

	if i>=0:
		a[:k+1]=a[:i+1]
	else:
		a[:k+1]=b[:j+1]
	return a

def main():
	a = [1,3,4,5,0,0,0,0]
	b = [2,4,5,6]
	print sortedMerge(a,b,3)

if __name__ == "__main__":
	main()
