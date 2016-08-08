#worst case O(n^2) but average runtime can be much better

def nearestGreater(l):
	lengthL = len(l)
	k=[None]*lengthL

	for i,num in enumerate(l):
		j1 = j2 = i
		while True:
			j1 -= 1
			j2 += 1
			if j1>0 or j2<lengthL:
				if j1>0 and l[j1]>num:
					k[i]=j1
					break
				elif j2<lengthL-1 and l[j2]>num:
					k[i]=j2
					break
			else:
				break
	return k

def main():
	l = [2,5,1,5,8,2,4]
	print l
	print nearestGreater(l)

if __name__ == "__main__":
	main()

