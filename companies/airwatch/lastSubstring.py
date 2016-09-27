def compute(s):
	length = len(s)
	i = length-1
	index = i
	while i>=0:
		if s[i]>=s[index]:
			index=i
		i-=1
	return s[index:]