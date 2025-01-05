from collections import deque
n,k=map(int,input().split())
d=deque([i for i in range(1,n+1)])
while len(d)>1:
    t=d[0]
    for _ in range(len(d) if k>len(d) else k): d.popleft()
    d.append(t)
print(d[0])