
def  maxValues(n, k):
    bits = sys.getsizeof(n)*8
    while 1<n:
        b = n
        for i in xrange(bits):
            