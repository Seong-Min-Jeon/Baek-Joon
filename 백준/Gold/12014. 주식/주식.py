from bisect import bisect_left as B
import sys
I=sys.stdin.readline
for k in range(int(I())):
    print(f'Case #{k+1}')
    a,b=map(int,I().split())
    m=[]
    for e in map(int,I().split()):
        i=B(m,e)
        if(i>=len(m)): m.append(e)
        else: m[i]=e
    print(0 if len(m)<b else 1)