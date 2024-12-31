from itertools import combinations
n,m=map(int,input().split())
h,c,d=[],[],[]
for i in range(n):
    t=list(map(int,input().split()))
    for j in range(n):
        if(t[j]==1): h.append((i,j))
        elif(t[j]==2): c.append((i,j))
t=list(combinations(c,m))
b=10**9
for g in t:
    for e in h:
        r=(1000,1000)
        for f in g:
            if(abs(e[0]-f[0])+abs(e[1]-f[1])<abs(e[0]-r[0])+abs(e[1]-r[1])):
                r=f
        d.append(abs(e[0]-r[0])+abs(e[1]-r[1]))
    b=min(b,sum(d))
    d.clear()
print(b)