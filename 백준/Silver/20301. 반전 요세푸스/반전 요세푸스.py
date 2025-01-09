from collections import deque
n,k,m=map(int,input().split())
d=deque([i for i in range(1,n+1)])
c,t=0,-1
for i in range(1,n+1):
    d.rotate(k*t)
    if(t==-1): print(d.pop())
    else: print(d.popleft())
    if(i%m==0): t*=-1