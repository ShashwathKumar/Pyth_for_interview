def groupAnagrams(l):
	d = {}
	for st in l:
		s = ''.join(sorted(st))
		if s not in d:
			d[s]=[st]
		else:
			d[s].append(st)
	lindex=0
	for ld in d.values():
		length = len(ld)
		l[lindex:lindex+length]=ld
		lindex+=length
	return l

def main():
	l = ['hi', 'ih', 'hello', 'olleh', 'hari', 'ahir', 'holle']
	print groupAnagrams(l)

if __name__ == "__main__":
	main()