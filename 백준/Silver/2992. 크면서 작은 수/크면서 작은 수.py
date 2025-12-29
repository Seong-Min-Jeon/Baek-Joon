from itertools import permutations as P
s=list(input().strip())
l=list(set([int(''.join(e)) for e in list(P(s,len(s)))]))
l.sort()
try: print(l[l.index(int(''.join(s)))+1])
except: print(0)