import sys
from collections import deque
ip=sys.stdin.readline
n,q=map(int,ip().split())
l=deque(map(int,ip().split()))
for _ in range(q):
    o=ip().split()
    if(o[0]=='1'):
        l[int(o[1])-1]+=int(o[2])
    elif(o[0]=='2'):
        s=int(o[1])
        l.rotate(s)
    elif(o[0]=='3'):
        s=int(o[1])
        l.rotate(-s)
for e in l:
    print(e,end=' ')