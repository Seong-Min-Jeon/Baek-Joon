import sys
import heapq
i=sys.stdin.readline
p=[]
m=[]
for _ in range(int(i())):
    a=int(i())
    if(a==0):
        if(len(p)==0 and len(m)==0): print(0); continue
        if(len(m)==0): print(heapq.heappop(p)); continue
        if(len(p)==0): print(heapq.heappop(m)*-1); continue
        if(m[0]<=p[0]): print(heapq.heappop(m)*-1); continue
        if(p[0]<m[0]): print(heapq.heappop(p)); continue
        continue
    if(a>0): heapq.heappush(p,a)
    else: heapq.heappush(m,a*-1)