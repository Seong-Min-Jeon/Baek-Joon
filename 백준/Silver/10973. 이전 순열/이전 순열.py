n=int(input()); l=[*map(int,input().split())]
if(sorted(l)==l): print(-1); exit()
k,v=0,0
for i in range(n):
    if(l[i]<v): k=i
    v=l[i]
t=sorted(l[k-1:].copy(),reverse=True)
v=t[t.index(l[k-1])+1]
t.remove(v)
print(*l[:k-1],v,*t)