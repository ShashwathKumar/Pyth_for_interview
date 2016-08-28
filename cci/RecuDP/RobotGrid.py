from collections import namedtuple

cnt=0

maze = []
maze.append([1, 0, 1, 1, 0])
maze.append([1, 1, 1, 1, 0])
maze.append([1, 0, 1, 1, 0])
maze.append([0, 1, 1, 0, 1])
maze.append([1, 1, 1, 1, 1])

Cell = namedtuple('Cell', ['r', 'c'])

def findPath(maze):
	rLen = len(maze)
	cLen = len(maze[0])

	destCell = Cell(rLen-1, cLen-1)
	srcCell  = Cell(0,0)
	path=[]

	return findPathRec(maze, srcCell, destCell, path)

def findPathRec(maze, srcCell, destCell, path):
	global cnt
	cnt+=1
	r = destCell.r
	c = destCell.c
	if r <0 or c<0 or not maze[r][c]:
		return False

	if destCell == srcCell:
		return True

	if findPathRec(maze, srcCell, Cell(r-1, c), path) or findPathRec(maze, srcCell, Cell(r, c-1), path):
		path.append(destCell)
	else:
		maze[r][c]=False

	return path

def main():
	path = findPath(maze)
	for cell in path:
		print cell
	print
	for l in maze:
		print l
	print
	print cnt

if __name__ == "__main__":
	main()
