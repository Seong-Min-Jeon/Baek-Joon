import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,k=F()
l=[tuple(F()) for _ in range(n)]
l+=[(int(I()),1e9) for _ in range(k)]
l.sort()
q=[]
r=0
for m,v in l:
    if(v==1e9 and q): r-=heapq.heappop(q)
    elif(v!=1e9): heapq.heappush(q,-v)
print(r)