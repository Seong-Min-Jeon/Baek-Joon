n=int(input())
l=list(map(int,input().split()))
v=[-1]*n
s,e=map(int,input().split())
q=[(s-1,0)]
v[s-1]=0
while q:
    p,c=q.pop(0)
    for i in range(p,n,l[p]):
        if(v[i]==-1): q.append((i,c+1)); v[i]=c+1
    for i in range(p,-1,-l[p]):
        if(v[i]==-1): q.append((i,c+1)); v[i]=c+1
if(v[e-1]==-1): print(-1)
else: print(v[e-1])