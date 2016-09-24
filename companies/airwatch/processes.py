def processes():
	ip  = raw_input()
	ipL = ip.split()
	n   = int(ipL[0])
	mem = int(ipL[1])
	time  = 0
	procL = []

	for i in xrange(n):
		ip  = raw_input()
		ipL = ip.split()
		procL.append((int(ipL[0]), int(ipL[1])))

	i = 0
	currMem = mem
	currProcs = set()
	time = 0
	minTime = 0
	while i<len(procL):
		procMem = procL[i][1]
		while currMem > procMem:
			currMem -= procMem
			currProcs[i]
			i+=1
		else:
			times   = map(lambda index: procL[index][0], currProcs)
			minTime = min(times)
			while memAvailable < memRequired:
				currMem -= minTime
				time += minTime
				for i in currProcs:
					procL[i][0]-=minTime



		


processes()