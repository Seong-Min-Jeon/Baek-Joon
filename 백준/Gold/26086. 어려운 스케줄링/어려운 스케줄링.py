import sys
from collections import deque as D
I=sys.stdin.readline
n,q,k=map(int,I().split())
s=D([])
r=0
l=[]
c=0
for _ in range(q):
    t=I().strip()
    if(t=='1'): c+=1
    l.append(t)
for t in l:
    m=0
    if(len(t)==1): t=int(t)
    else: t,m=map(int,t.split())
    if(t==0):
        if(r): s.appendleft(m)
        else: s.append(m)
    elif(t==1):
        if(c==1):
            if(r): s=D(sorted(list(s)))
            else: s=D(sorted(list(s),reverse=True))
        else:
            c-=1
    else:
        r=abs(r-1)
if(r): print(s[k-1])
else: print(s[-k])