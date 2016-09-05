from math import log

def lg(n):
	return int(log(n,2))

def xly(m,n):
	(m,n) = (n,m) if n<m else (m,n)
	_sum=0
	while m>1:
		print m,n
		tmp = lg(m)
		_sum += n<<tmp
		m-=2**tmp
	_sum += n if m else 0
	return _sum

def xly2(m, n):
	(m,n) = (n,m) if n<m else (m,n)  #do this in order to get lg(s)
	print m,n
	if m>1:
		tmp = lg(m)
		return (n<<tmp) + xly2(m-2**tmp, n)  #+ has more precedence over << ***
	return n if m else 0

def main():
	print xly2(6,13)
	print xly(12,13)

if __name__ == "__main__":
	main()