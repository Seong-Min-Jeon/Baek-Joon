def g():
    for j,e in ((0,'A'),(1,'C'),(2,'G'),(3,'T')):
        if(d[e]<p[j]): return 0
    return 1
f=lambda:map(int,input().split())
n,m=f()
s=input().strip()
p=[*f()]
d={}
for e in ('A','C','G','T'): d[e]=s[:m].count(e)
c=0
c+=g()
for i in range(n-m):
    d[s[i]]-=1
    d[s[i+m]]+=1
    c+=g()
print(c)