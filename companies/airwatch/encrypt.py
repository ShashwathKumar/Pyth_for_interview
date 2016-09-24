def encrypt():
	s = raw_input()
	l = []
	for c in s:
		ascii = ord(c)
		if ascii<97 or ascii>122:
			l.append(c)
			continue
		val = ascii-97
		l.append(str(val))
		if val>9:
			l.append('#')
	op = ''.join(l)
	print(op)

encrypt()