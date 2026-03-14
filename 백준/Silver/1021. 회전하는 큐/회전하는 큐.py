from collections import deque as D
n,m=map(int,input().split())
p=[*map(int,input().split())]
d=D([i+1 for i in range(n)])
c=0
for e in p:
    i=d.index(e)
    c+=min(i,len(d)-i)
    if(i<=len(d)-i): d.rotate(-i)
    else: d.rotate(len(d)-i)
    d.popleft()
print(c)