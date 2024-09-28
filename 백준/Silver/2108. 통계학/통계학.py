import sys
i=sys.stdin.readline
l=[]
d={}
for _ in range(int(i())):
    a=int(i())
    l.append(a)
    d[a]=d.get(a,0)+1
print(round(sum(l)/len(l)))
l.sort()
print(l[len(l)//2])
m=0
for v in d.values():
    m=max(m,v)
t=[]
for k in d:
    if(d[k]==m):
        t.append(k)
t.sort()
if(len(t)>1): print(t[1])
else: print(t[0])
print(max(l)-min(l))