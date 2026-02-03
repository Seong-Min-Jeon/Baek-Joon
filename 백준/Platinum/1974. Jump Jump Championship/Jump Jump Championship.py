from bisect import bisect_left as B
import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    l=[*map(int,I().split())]
    m,d=[],[]
    for e in l:
        i=B(m,e)
        if(len(m)<=i): m.append(e)
        else: m[i]=e
        d.append(i+1)
    c=len(m)
    print(c)
    t=[]
    for i,e in enumerate(reversed(d)):
        if(e==c): t.append(n-i); c-=1
    print(*reversed(t))