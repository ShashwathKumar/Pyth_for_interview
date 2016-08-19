def funpan(s):
	d = {}
	for c in s:
		if c in d:
			d[c]=1
		else:
			d[c]+=1
	odds = []
	evens = []
	for k,v in d.items():
		if v%2==0:
			evens.append((k,v))
		else:
			odds.append((k,v))
	odds  = sorted(odds,  key=lambda x: x[1], reverse=True)
	evens = sorted(evens, key=lambda x: x[1], reverse=True)
	a = formPal(odds, evens)

def formPal(odds, evens):
	l = []
	odd = odds.pop(0)
	oddFirstHalf = odd[1]/2
	
	l.append(odd[:oddFirstHalf])
	for k,v in evens:
		halfv = v/2
		l.append(k*halfv)
		v = halfv

	l.append(odd[oddFirstHalf])
	for k,v in reversed(evens):
		l.append(k*v)

	l.append(odd[oddFirstHalf+1:])
	return ''.join(l)

def main():
	print funpal(s)

if __name__ == "__main__":
	main()