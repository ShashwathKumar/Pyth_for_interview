def sort012(l):
  p = 0
  q = len(l)-1
  i=0
  
  while i<=q:
    if l[i]==0:
      l[i], l[p] = l[p], l[i]
      p+=1
    elif l[i]==2:
      l[i], l[q] = l[q], l[i]
      q-=1
      i-=1
    #increment
    i+=1

def main():
  l = [0, 1, 0, 1, 2, 2, 1, 0]
  sort012(l)
  print l

if __name__ == "__main__":
  main()
