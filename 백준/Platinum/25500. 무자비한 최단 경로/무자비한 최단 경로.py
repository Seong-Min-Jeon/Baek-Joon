import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,k=f()
t=[]
for i in range(n):
    a,b,c=f()
    t.append((a,b,c,i+1))
l=[[] for _ in range(n+k+1)]
t.sort()
for i in range(n-1):
    a,_,_,x=t[i]
    c,_,_,y=t[i+1]
    l[x].append((y,abs(a-c)))
    l[y].append((x,abs(a-c)))
t.sort(key=lambda x:x[1])
for i in range(n-1):
    _,a,_,x=t[i]
    _,c,_,y=t[i+1]
    l[x].append((y,abs(a-c)))
    l[y].append((x,abs(a-c)))
for e in t:
    _,_,a,x=e
    l[x].append((n+(a%k)+1,a))
    l[n+(k-a%k)%k+1].append((x,a))
r=[1e99]*(n+k+1)
r[1]=0
q=[(0,1)]
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(r[i]>d+e):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
for i in range(1,n+1):
    print(r[i])