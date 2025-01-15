import math
from itertools import permutations as P
l,s,p,r=[],[],[],[]
for i in range(4):
    l.append(list(map(int,input().split())))
    if(i==0): s=l.pop()
p=list(P(l,3))
for e in p:
    c=s.copy()
    t=[]
    for f in e:
        t.append(math.dist(c,f))
        c=f
    r.append(int(sum(t)))
print(min(r))