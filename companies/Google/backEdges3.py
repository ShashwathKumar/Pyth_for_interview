def backEdges(G, start):
	stack     = []
	backEdgesSet = set()
	start.visited=True #start is a parent now

	for node in G[start.name]:
		if node.visited==None:
			backEdgesSet |= backEdges(G, node) #unioning the sets
		elif node.visited==True:
			backEdgesSet.add(start.name+node.name)

	start.visited=False #start is no longer a parent but is a visited node
	return backEdgesSet

class Node(object):
	def __init__(self, name):
		self.name = name
		self.visited  = None
		#self.parents  = set()

def getGraph():
	G = {}
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')

	G['a']=[b, c]
	G['b']=[g, f]
	G['c']=[e, d]
	G['d']=[c]
	G['e']=[b, f]
	G['f']=[]
	G['g']=[b, f]

	# G['c']=[e, d, b]
	# G['d']=[c, e]
	# G['e']=[b, f, a]
	# G['f']=[a]

	return G, a

def main():
	G, start = getGraph()
	print backEdges(G, start)

if __name__ == "__main__":
	main()