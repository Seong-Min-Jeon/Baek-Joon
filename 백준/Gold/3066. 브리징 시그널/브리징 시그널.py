from bisect import bisect_left as B
import sys
I=sys.stdin.readline
for _ in range(int(I())):
    l=[int(I()) for _ in range(int(I()))]
    m=[]
    for e in l:
        i=B(m,e)
        if(i>=len(m)): m.append(e)
        else: m[i]=e
    print(len(m))