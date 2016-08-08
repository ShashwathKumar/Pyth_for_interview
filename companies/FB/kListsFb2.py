#my lovely classic code with generator and iterator :)
#much more awesome than my first code in kListsFb.py

def myIter(l):
	while any(map(lambda x: len(x)>0, l)):
		myMin = min([x[0] for x in l if x])
		for listo in l:
			if listo:
				if myMin==listo[0]:
					yield listo.pop(0)

def main():
	l = [[1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8, 8], [1, 2, 2, 3, 3, 4, 5, 6]]
	m = myIter(l)
	while True:
		try:
			print next(m)
			usrIp = raw_input('Do u want more (y/n): ')
			if usrIp.lower() == 'y':
				continue
			else:
				print 'Bye'
				break
		except:
			print 'Sorry..!! Thats all I had'
			break

if __name__ == '__main__':
	main()