def iterGen(i1, i2, i3):
	kmap = {
		0: i1,
		1: i2,
		2: i3
	}
	keys = kmap.keys()
	kLen = len(keys)

	i = 0
	while i<kLen:
		#print i, keys
		toYield = next(kmap[keys[i]], None)
		if toYield == None:
			keys.pop(i)
			kLen-=1
			continue
		#print toYield
		yield toYield
		i+=1
		if i==kLen:
			i=0

def main():
	l1 = [1, 2, 3, 4]
	l2 = [7, 8, 9, 0]
	l3 = [-1, -2, -3, -4, -5, -6, -7]
	i1 = iter(l1)
	i2 = iter(l2)
	i3 = iter(l3)

	g = iterGen(i1, i2, i3)

	for n in g:
		print n,

if __name__ == "__main__":
	main()