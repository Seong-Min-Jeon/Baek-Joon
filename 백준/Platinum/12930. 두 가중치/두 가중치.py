import heapq
def f(s,d):
    q=[(0,0,s)]
    v=[1e9]*n
    while q:
        x,y,p=heapq.heappop(q)
        if(v[p]<x*y or (p not in a)): continue        
        for k in a[p]:
            t,i,j=k
            if(v[t]>(x+i)*(y+j)): v[t]=(x+i)*(y+j); q.append((x+i,y+j,t))
    if(v[d]==1e9): return -1
    else: return v[d]
n=int(input())
a={}
for i in range(2*n):
    for j,e in enumerate(list(input().strip())):
        if(e=='.'): continue
        if(i<n):
            if(i not in a): a[i]=[[j,int(e)]]
            else: a[i].append([j,int(e)])
        else:
            for k in a[i-n]:
                if(k[0]==j): k.append(int(e))
print(min(f(0,1),f(1,0)))