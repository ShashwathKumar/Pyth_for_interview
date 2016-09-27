def rollingString(s, operations):
	l = list(s)
	for st in operations:
		op = st.split()
		i = int(op[0])
		j = int(op[1])
		for x, c in enumerate(l[i:j+1]):
			if op[2]=='L':
				l[i+x] = chr(ord(c)-1)
			elif op[2]=='R':
				l[i+x] = chr(ord(c)+1)

			if l[i+x]=='`':
				l[i+x]='z'
			elif l[i+x]=='{':
				l[i+x]='a'
	return ''.join(l)


