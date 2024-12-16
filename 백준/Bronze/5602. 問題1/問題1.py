a,b=map(int,input().split())
t=(0 for _ in range(b))
for _ in range(a):
    t=tuple(sum(e) for e in zip(t,map(int,input().split())))
t=list(t)
l=[]
for _ in range(b):
    l.append(t.index(max(t))+1)
    t[t.index(max(t))]=-1
print(*l)