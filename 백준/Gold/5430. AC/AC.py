import sys
from collections import deque
I=sys.stdin.readline
for _ in range(int(I())):
    r=1
    f=list(I().strip())
    if(f.count('D')>int(I())): I(); print('error'); continue
    t=I().strip()
    d=deque(t[1:len(t)-1].split(','))
    for e in f:
        if(e=='R'): r*=-1
        else:
            if(r==1): d.popleft()
            else: d.pop()
    l=list(d)
    if(r==-1): l.reverse()
    if(len(l)==0 or l==['']): print('[]')
    else: 
        print('[', end='')
        t=l.pop()
        for e in l:
            print(e, end=',')
        print(t, end='')
        print(']')