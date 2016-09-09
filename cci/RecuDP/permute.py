#the basic trick in permute is that the length of each permutation is fixed
#the difference between this permute and keypad is that --
#in keypad u just go from number to number one after the other
#    -- the list u r recursing through and the string u r iterating through are different
#in this permute the string u r recursing through and the string u r iterating through are same
#    -- hence u have to use removeCh instead of basic s[1:]

def permute(s):
	ansL = []

	for i, c in enumerate(s):
		tmp = c
		if len(s)>1:
			ansL += permute_rec(removeCh(s, i), tmp)
		else:
			ansL.append(tmp)
	return ansL

def permute_rec(s, c):
	tmpL = []

	for i, ch in enumerate(s):
		tmp = c + ch
		if len(s)>1:
			tmpL += permute_rec(removeCh(s, i), tmp)
		else:
			tmpL.append(tmp)
	return tmpL

def removeCh(s, i):
	if i==0:
		return s[1:]
	elif i==len(s)-1:
		return s[:-1]
	else:
		return s[:i]+s[i+1:]

def main():
	s = 'ab'
	print permute(s)

if __name__ == "__main__":
	main()