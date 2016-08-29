from collections import namedtuple
import sys

Cell = namedtuple('Cell', ['r', 'c'])
fruits = 0

maze = []
maze.append([1, 0, 1, 0, 1])
maze.append([1, 0, 1, 0, 1])
maze.append([1, 0, 1, 0, 0])
maze.append([1, 0, 1, 0, 1])
maze.append([1, 1, 1, 1, 1])

visitedMaze = []
for i in xrange(5):
	visitedMaze.append([0, 0, 0, 0, 0])

def findPath(maze):
	rLen = len(maze)
	cLen = len(maze[0])

	destCell = Cell(rLen-1, cLen-1)
	srcCell  = Cell(0, 0)
	path = []

	findValRec(maze, srcCell, destCell)
	printMaze()
	return findPathRec(maze, path, srcCell, destCell)

def findValRec(maze, srcCell, destCell):
	r = destCell.r
	c = destCell.c

	if c<0 or r<0 or visitedMaze[r][c]:
		return
	visitedMaze[r][c]=1

	if srcCell == destCell:
		return

	findValRec(maze, srcCell, Cell(r-1, c))
	findValRec(maze, srcCell, Cell(r, c-1))
		
	if c-1 < 0:
		maze[r][c] += maze[r-1][c]
	elif r-1 < 0:
		maze[r][c] += maze[r][c-1]
	else:
		maze[r][c] += max(maze[r-1][c], maze[r][c-1])

def findPathRec(maze, path, srcCell, destCell):
	#in this kinda matrix traversal u should go as right as possible
	#I think somehow heavy weights get accumulated down
	global fruits
	r = srcCell.r
	c = srcCell.c

	if maze[r][c]:
		fruits+=1
	path.append(srcCell)

	if srcCell==destCell:
		return

	if c+1>destCell.c:
		right = -sys.maxint -1
		down  = maze[r+1][c]
	elif r+1>destCell.r:
		down  = -sys.maxint -1
		right = maze[r][c+1]
	else:
		right = maze[r][c+1]
		down  = maze[r+1][c]

	if right == max(right,down):
		findPathRec(maze, path, Cell(r,c+1), destCell)
	else:
		findPathRec(maze, path, Cell(r+1,c), destCell)

	return path

def printMaze():
	for l in maze:
		print l
	print

def main():
	print findPath(maze)
	print fruits

if __name__ == "__main__":
	main()