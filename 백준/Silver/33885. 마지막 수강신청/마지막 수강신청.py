def f(b,s,v,p):
    global a
    a=max(a,b)
    for i in range(p+1,n):
        t=d[i]
        if(i in s): continue
        if(len(set(t[1:]).intersection(v))!=0): continue
        f(b+t[0],s.union({i}),v.union(set(t[1:])),i)
n,m=map(int,input().split())
d={}
for i in range(n):
    t=input().strip().split()
    d[i]=[int(t[0])]
    for j in range(int(t[1])):
        d[i].append((t[2+2*j],t[3+2*j]))
a=0
f(0,set(),set(),-1)
print('YES' if a>=m else 'NO')