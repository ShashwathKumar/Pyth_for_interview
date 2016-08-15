cntr = 0
def search_with_mid(l, st, minv, maxv, mid):
        #print 'search_with_mid', mid
        if l[mid] < st:
            minv = mid+1
            return search_rec(l, st, minv, maxv)
        elif l[mid] > st:
            maxv = mid-1
            return search_rec(l, st, minv, maxv)
        else:
            return mid

def sparseSearch(l, st):
    if not l or not st:
        return 'Invalid Input'
    return search_rec(l, st, 0, len(l)-1)
    
def search_rec(l, st, minv, maxv):
    global cntr
    cntr+=1
    if cntr==10:
        return None
    #print l, st, minv, maxv
    if minv>maxv:
        return None
    mid = (minv+maxv)/2
    length = len(l)-1
    
    if l[mid]:
        return search_with_mid(l, st, minv, maxv, mid)
    else:
        left = mid-1
        right = mid+1
        while True:
               if l[left] and not left < 0:
                   mid = left
                   return search_with_mid(l, st, minv, maxv, mid)
               elif l[right] and not right > length-1:
                    mid = right
                    return search_with_mid(l, st, minv, maxv, mid)
               else:
                    if left <= 0 and right >= length-1:
                        #print 'Lost it', 'left', left, 'right', right
                        return None
                    if left > 0:
                        left -= 1
                    if right < length-1:
                        right+=1
                    
def main():
    l = ['', '', '', 'hello', '', '', 'hi', '', '', 'how', '', '', 'hy', '', '', 'kite']
    eindex = sparseSearch(l, '')
    print eindex if eindex else 'Not Found'

if __name__ == "__main__":
    main()
                   
