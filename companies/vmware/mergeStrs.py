def  mergeStrings(a, b):
    lena = len(a)
    lenb = len(b)
    minlen = min(lena, lenb)
    l = []
    
    i = 0
    while i < minlen:
        l.extend([a[i], b[i]])
        i+=1
    if lena!=lenb:
        if minlen==lena:
            l.extend(b[i:])
        elif minlen==lenb:
            l.extend(a[i:])
    return ''.join(l)