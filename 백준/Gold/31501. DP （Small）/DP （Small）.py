from bisect import bisect_left
import sys
I=sys.stdin.readline
n,q=map(int,I().split())
l=list(map(int,I().split()))
m=[-e for e in l]
m.reverse()
a,b=[],[]
x,y=[],[]
for e in l:
    i=bisect_left(b,e)
    if(i>=len(b)): b.append(e)
    else: b[i]=e
    a.append(i)
for e in m:
    i=bisect_left(y,e)
    if(i>=len(y)): y.append(e)
    else: y[i]=e
    x.append(i)
x.reverse()
for _ in range(q):
    i=int(input())-1
    print(a[i]+x[i]+1)