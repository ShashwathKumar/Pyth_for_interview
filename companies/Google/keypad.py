kmap = {
	1: 'abc',
	2: 'def',
	3: 'ghi',
	4: 'jkl',
	5: 'mno',
	6: 'pqrs',
	7: 'tuv',
	8: 'wxyz'
}

def isValid(s):
	return True

def keypad(l):
	ansL = []

	for c in kmap[l[0]]:
		if len(l)>1:
			tmp  = c
			ansL.extend(keypad_rec(l[1:], c))
		elif isValid(c):
			ansL.append(c)

	return ansL

def keypad_rec(l, c):
	tmpAnsL = []

	for ch in kmap[l[0]]:
		tmp = c+ch
		if len(l)>1:
			tmpAnsL.extend(keypad_rec(l[1:], tmp))
		elif isValid(tmp):
			tmpAnsL.append(tmp)

	return tmpAnsL

def main():
	l = [1, 2, 3]
	print keypad(l)

if __name__ == "__main__":
	main()