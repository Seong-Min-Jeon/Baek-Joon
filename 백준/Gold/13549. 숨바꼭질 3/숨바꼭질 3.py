import heapq
n,k=map(int,input().split())
F=1e8
r=[F for _ in range(10**5+1)]
q=[(0,n)]
r[n]=0
while q:
    t,p=heapq.heappop(q)
    if(r[p]<t): continue
    if(p-1>=0 and t+1<r[p-1]): 
        r[p-1]=t+1; heapq.heappush(q,(t+1,p-1))
    if(p+1<=10**5 and t+1<r[p+1]): 
        r[p+1]=t+1; heapq.heappush(q,(t+1,p+1))
    if(2*p<=10**5 and t<r[2*p]): 
        r[2*p]=t; heapq.heappush(q,(t,2*p))
print(r[k])