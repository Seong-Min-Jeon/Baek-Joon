n,m=map(int,input().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
m=0
def f(s,i,c):
    global m
    if(i==n): m=max(m,c); return
    for p in l[i]:
        if(i in s or p in s): continue
        s.add(i); s.add(p)
        f(s,i+1,c+2)
        s.remove(i); s.remove(p)
    f(s,i+1,c)
f(set(),0,0)
if(m<n): m+=1
print(m)