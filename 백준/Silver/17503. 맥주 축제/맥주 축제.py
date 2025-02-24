import heapq
import sys
I=sys.stdin.readline
n,m,k=map(int,I().split())
l=[tuple(map(int,I().split())) for _ in range(k)]
l.sort(key=lambda x: -x[1])
h=[]
s=0
while l:
    t=l.pop()
    if(len(h)<n): heapq.heappush(h,t); s+=t[0]
    if(len(h)==n):
        if(s>=m): print(t[1]); exit()
        else: s-=heapq.heappop(h)[0]
print(-1)