import heapq
I=input
n,m=map(int,I().split())
x,y=[],[]
for _ in range(n):
    i=list(I())
    x.append(list(map(int,i)))
    y.append(list(map(lambda a: int(a)/2,i)))
r=[[1e9 for _ in range(m+1)] for _ in range(n)]
q=[(0,0,0)]
r[0][0]=0
while q:
    t,p,c=heapq.heappop(q)
    if(r[p][c]<t): continue
    for i,e in enumerate(x[p]):
        if(r[i][c]>t+e):
            r[i][c]=t+e
            heapq.heappush(q,(t+e,i,c))
    for i,e in enumerate(y[p]):
        if(c<m and r[i][c+1]>t+e):
            r[i][c+1]=t+e
            heapq.heappush(q,(t+e,i,c+1))
print(min(r[1]))