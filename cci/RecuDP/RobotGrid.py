from math import ceil

o = [(3,3), (4,3)]

def RobotGridRec(r, c, prevStep):
	ratio = 0 #just initializing it
    if (not r==0) and (not c==0):
		ratio = float(r)/float(c)

	if r==0 and c==0:
		print "Goal reached..!!"
	elif c==0:
		print 'move '+r+ 'steps down'
	elif r==0:
		print 'move '+c+ 'steps right'
	elif prevStep == 'r':
		steps = ceil(ratio)
		print 'move '+ str(steps)+ ' steps down'
		RobotGridRec(r-steps, c, 'd')
	elif prevStep == 'd' or prevStep == None:
		steps = ceil(1/ratio)
		print 'move '+ str(steps)  + ' steps right'
		RobotGridRec(r, c-steps, 'r')


def RobotGrid(r, c):
	RobotGridRec(r, c, None)

def main():
	r = 5
	c = 10
	RobotGrid(5, 10)

if __name__ == "__main__":
	main()
