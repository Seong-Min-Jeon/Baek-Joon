import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(m):
    x,y=-b[i],a[i]
    if(y-100>x): x=y-100
    heapq.heappush(l,(x,y))
for _ in range(n*24):
    x,y=heapq.heappop(l)
    y-=x
    if(y-100>x): x=y-100
    if(y>100): x,y=0,100
    heapq.heappush(l,(x,y))
s=0
for e in l:
    s+=e[1]
print(s)