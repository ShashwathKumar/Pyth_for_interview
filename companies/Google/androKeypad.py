# 0  1  2 

# 3  4  5

# 6  7  8

# 0 -> 1 -> 2  (OK)
# 0 -> 1 -> 0  (NO)
# 1 -> 2 -> 0

# 0 -> 7
# 0 -> 5
# 0 -> 8  (NO)

# 0 -> 1 -> 2 -> 3
# 3 -> 2 -> 1 -> 0

# Requirements of a lock pattern:
# Minimum connect 4 points, (maximum 9)
# Two points are connectable if a line can be drawn between them
# Can't revisit a point


# 0 ---(2, 6, 8)

# 0 -> 1 -> 2

# 0  1  2 

# 3  4  5

# 6  7  8

# 1 -> 2 -> 0
from copy import deepcopy

def lock_patterns():
   forbidden = { 0: set([2, 6, 8]),
                 1: set(7),
                 2: set([0, 6, 8]),
                 3: set([5]),
                 4: set(),
                 5: set([3]),
                 6: set([0, 2, 8]),
                 7: set([1]),
                 8: set([0, 2, 6]),
                }
    l = [i for i in xrange(9)]
    cnt = 0

    for i, n in enumerate(l):
        f = deepcopy(forbidden)
        f = clearPath(n, f)
        cnt += lock_pattern_rec(l[0:i].extend(l[i+1:]), n, f)

    return cnt

def lock_pattern_rec(l, e, fprev):
    if len(l)==1:
        return 1

    cnt = 0
    if len(l)<=5:
        cnt+=1
    for i, n in enumerate(l):
        f = deepcopy(fprev)
        if n in f[e]:
            continue
        else:
            f = clearPath(n, f)
            cnt += lock_pattern_rec(l[0:i].extend(l[i+1:], n, f)

    return cnt

def clearPath(n, f):
    if n == 1:
       f[0].remove(2)
       f[2].remove(0)
    elif n == 3:
       f[6].remove(0)
       f[0].remove(6)
    elif n == 5:
       f[8].remove(2)
       f[2].remove(8)
    elif n == 7:
       f[8].remove(6)
       f[6].remove(8)
    elif n == 4:
       f[0].remove(8)
       f[8].remove(0)
       f[2].remove(6)
       f[6].remove(2)
      

