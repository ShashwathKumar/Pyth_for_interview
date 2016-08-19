def  buildSubsequences( s):
    xlist = []
    length = len(s)
    combs = (2**length)-1
    for i in range(1, combs+1):
    	st=''
    	l =[]
        for j, c in enumerate(s):
        	if i>>j & 1:
        		l.append(c)
        st = ''.join(l)
        xlist.append(st)
    return xlist

def main():
	print buildSubsequences('abc')

if __name__ == "__main__":
	main()