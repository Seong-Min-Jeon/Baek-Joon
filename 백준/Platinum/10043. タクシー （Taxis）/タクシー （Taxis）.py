import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
t={}
z=0
for i in range(n):
    a,b=F()
    t[i+1]=[a,b]
    z=max(z,b)
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=F()
    l[a].append(b)
    l[b].append(a)
r=[[1e99]*(z+1) for _ in range(n+1)]
r[1][0]=0
q=[(t[1][0],t[1][1],1)]
while q:
    d,k,p=heapq.heappop(q)
    if(r[p][k]<d): continue
    for i in l[p]:
        if(r[i][k-1]>d):
            r[i][k-1]=d
            if(k>1):
                heapq.heappush(q,(d,k-1,i))
        if(r[i][t[i][1]]>d+t[i][0]):
            r[i][t[i][1]]=d+t[i][0]
            heapq.heappush(q,(d+t[i][0],t[i][1],i))
print(min(r[-1]))