def cntChars(st):
	d = {}
	for c in st:
		if c in d:
			d[c]+=1
		else:
			d[c]=1
	return d

def groupAnagrams(l):
	d  = {}
	dl = []
	tmpdl = []
	fl = []

	for st in l:
		d = cntChars(st)
		dl.append(d)

	while True:
		if not dl:
			break
		xd = dl[0]
		tmpdl.append(0)
		for j,yd in enumerate(dl[1:]):
			if xd==yd:
				tmpdl.append(j+1) #this enumerate
		for j in tmpdl:
			fl.append(l[j])
		for j in reversed(tmpdl): #always pop() from reverse order, else indices change
			l.pop(j)
			dl.pop(j)
		tmpdl=[]

	return fl

def main():
	l = ['hi', 'ih', 'hello', 'olleh', 'hari', 'ahir', 'holle']
	print groupAnagrams(l)

if __name__ == "__main__":
	main()