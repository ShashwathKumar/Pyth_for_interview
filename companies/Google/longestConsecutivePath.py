class Node(object):
	def __init__(self, val):
		self.val = val
		self.children = []

def longestConsecutivePath(root):
	return longestConsecutivePath_rec(root, root.val-1, 0, [])

def longestConsecutivePath_rec(root, prevNum, prevCnt, prevPath):
	if not root:
		return prevCnt, prevPath

	cnt  = 1
	path = [root.val]

	if root.val==prevNum+1:
		cnt  = prevCnt+1
		path = prevPath
		path.append(root.val)

	for node in root.children:
		cntRet, pathRet = longestConsecutivePath_rec(node, root.val, cnt, path)
		if cnt<cntRet:
			cnt  = cntRet
			path = pathRet

	return max((cnt, path), (prevCnt, prevPath))

def getTree():
	a = Node(1)
	b = Node(2)
	c = Node(5)  ###
	d = Node(4)
	e = Node(10)
	f = Node(5)
	g = Node(6)
	h = Node(4)

	i = Node(7)
	j = Node(9)  ###
	k = Node(11)
	l = Node(13)
	m = Node(9)
	n = Node(9)
	o = Node(10)
	p = Node(11)
	q = Node(11)

	a.children = [b,i,n]
	b.children = [f,c,h]
	c.children = [d]
	d.children = [e]
	f.children = [g]
	i.children = [j]
	j.children = [k,l,m]
	n.children = [o,q]
	o.children = [p]

	return a

def main():
	root = getTree()
	print longestConsecutivePath(root)

if __name__=="__main__":
	main()