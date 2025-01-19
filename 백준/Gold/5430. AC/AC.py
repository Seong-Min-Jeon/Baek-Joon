import sys
from collections import deque
I=sys.stdin.readline
for _ in range(int(I())):
    r=1
    f=list(I().strip())
    n=int(I())
    if(f.count('D')>n): I(); print('error'); continue
    if(n==0): I(); print('[]'); continue
    d=deque(map(int,I().strip()[1:-1].split(',')))
    for e in f:
        if(e=='R'): r*=-1; continue
        if(r==1): d.popleft()
        else: d.pop()
    l=list(d)
    if(r==-1): l.reverse()
    print(str(l).replace(' ',''))