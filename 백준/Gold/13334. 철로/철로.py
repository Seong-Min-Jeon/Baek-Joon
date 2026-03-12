import sys
import heapq
I=sys.stdin.readline
l=[]
for _ in range(int(I())):
    a,b=map(int,I().split())
    l.append((min(a,b),max(a,b)))
l.sort(key=lambda x:x[1])
d=int(I())
q=[l[0][0]]
l.pop(0)
m=0
for e in l:
    a,b=e
    heapq.heappush(q,a)
    while q:
        t=heapq.heappop(q)
        if(t>=b-d): heapq.heappush(q,t); break
    m=max(m,len(q))
print(m)