from collections import deque
n,k,m=map(int,input().split())
d=deque([i for i in range(1,n+1)])
c,t=0,1
for i in range(1,n+1):
    if(t==1): 
        for _ in range(k):
            d.append(d.popleft())
        print(d.pop())
    else:
        for _ in range(k):
            d.appendleft(d.pop())
        print(d.popleft())
    if(i%m==0): t*=-1