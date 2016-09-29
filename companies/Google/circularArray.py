def singleCycle(arr):
    lengthArr = len(arr)
    tmpArr    = [False for i in xrange(lengthArr)]
    index     = 0 #just chose to start from 0 to keep it simple

    for n in arr:
        index+=n
        if index>lengthArr-1:
            index %= lengthArr
        elif index<-lengthArr:
            index *= -1
            index %= lengthArr
            index *= -1
            
        if tmpArr[index]==False:
            tmpArr[index]=True
        else:
            #return False if any of the elements were visited twice
            return False
   
    #return False if any of the elements were not visited
    if False in tmpArr:
        return False

    #return True if it surpasses above False checkpoints
    return True
