def  maxLength(a, k):
	s = sorted(a)
	total = 0
	wrds  = 0
	for n in s:
		total+=n
		if total<=k:
			wrds+=1
		else:
			break
	return wrds


from heapq import heappush, heappop

def maxLength(a, k):
	heap  = []
	total = 0
	wrds  = 0
	for n in a:
		heappush(heap, n)

	while True:
		nextMin = heappop(heap)
		total+=nextMin
		if total<=k:
			wrds+=1
		else:
			break
	return wrds

def maxLength(a, k):
	heap  = []
	total = 0
	wrds  = 0
	for n in a:
		if heap and n<=-heap[0] and total>=k:
			total+=heap[0] #heap[0] is negative here
			total+=n
			heappop(heap)
			heappush(heap, -n)
		else:
			total+=n
			if total<=k:
				heappush(heap, -n)
				wrds+=1
		print total
	return wrds


#-------------------------------------------------------

def maxLength(a, k):
	heap  = []
	total = 0
	wrds  = 0
	for n in a:
		if heap and n<=-heap[0] and total>=k:
			total+=heap[0] #heap[0] is negative here
			total+=n
			heappop(heap)
			heappush(heap, -n)
		elif total<k:
			total+=n
			if total<=k:
				heappush(heap, -n)
				wrds+=1
		print total
	return wrds


#-------------------------------------------------------

def maxLength(a, k):
	heap  = []
	total = 0
	wrds  = 0
	for n in a:
		if heap and n<-heap[0] and (total>=k or total+n>k):
			total+=heap[0] #heap[0] is negative here
			total+=n
			heappop(heap)
			heappush(heap, -n)
		elif total<k:
			total+=n
			if total<=k:
				heappush(heap, -n)
				wrds+=1
		print total
	return wrds


#-------------------------------------------------------

def maxLength(a, k):
	heap  = []
	total = 0
	wrds  = 0
	for n in a:
		if heap and n<-heap[0] and total+n>k:
			total+=heap[0] #heap[0] is negative here
			total+=n
			heappop(heap)
			heappush(heap, -n)
		elif total+n<=k:
			total+=n
			heappush(heap, -n)
			wrds+=1
		print len(heap)
		print total
	return wrds

#-------------------------------------------------------
#final code

    static int maxLength(int[] a, int k) {
        int i1=0;
        int i2=1;
        int total=a[i1];
        int wrdsCnt=0;
        while(i1 < i2 && i2 < a.length){
	       if(total+a[i2] <=k){
		      total+=a[i2];
		      i2++;
	       }else{
		      total-=a[i1];
		      wrdsCnt = wrdsCnt > i2-i1? wrdsCnt : i2-i1;
		      i1++;
	       }
        }
        wrdsCnt = wrdsCnt > i2-i1? wrdsCnt : i2-i1;
        return wrdsCnt;
       }
#-------------------------------------------------------
    # static int maxLength(int[] a, int k) {
    #     int lengtha = a.length;
    #     Arrays.sort(a);
    #     int total=0, wrds=0;
    #     for(int i = 0 ; i < a.length ;i++){
            
    #         total+=a[i];
    #         System.out.println(a[i] + " " + total + " " + wrds);
    #         if(total<=k){
    #             wrds+=1;
    #         }else{
    #             break;
    #         }
    #     }
    #     return wrds;
    # }

#-------------------------------------------------------
#Ashwin expt

def maxLength(a, k):
	heap  = []
	total = 0
	wrds  = 0
	for n in a:
		if heap and n<-heap[0] and total+n+heap[0]>k:
			total+=heap[0] #heap[0] is negative here
			total+=n
			heappop(heap)
			heappush(heap, -n)
		elif total+n<=k:
			total+=n
			heappush(heap, -n)
			wrds+=1
		print total
		print len(heap)
	return wrds