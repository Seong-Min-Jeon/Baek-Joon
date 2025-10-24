import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n=int(I())
s,z=F()
m=int(I())
l=[]
for _ in range(m):
    h,t,a,b=F()
    l.append((a,b,h,t))
    l.append((b,a,h,t))
r=[1e99]*(n+1)
r[s]=0
q=[(0,s)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,j,h,t in l:
        if(p<i or p-i+h>n): continue
        if(r[p-i+j]>d+t):
            r[p-i+j]=d+t
            heapq.heappush(q,(d+t,p-i+j))
print(r[z] if r[z]!=1e99 else -1)