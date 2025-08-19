import heapq
n=int(input())
x,y=[[]],[0]
for i in range(n):
    d,m,*f=map(int,input().split())
    x.append(f)
    y.append(d)
q=[(0,1)]
r=[1e9]*(n+1)
r[1]=0
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for e in x[p]:
        if(r[e]>d+y[p]):
            r[e]=d+y[p]
            heapq.heappush(q,(r[e],e))
print(max([r[i]+y[i] for i in range(1,n+1)]))