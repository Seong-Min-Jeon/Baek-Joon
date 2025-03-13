from bisect import bisect_left
n=int(input())
l=[tuple(map(int,input().split())) for _ in range(n)]
l.sort()
b=[e[1] for e in l]
m=[]
d=[]
for e in b:
    i=bisect_left(m,e)
    if(len(m)<=i): m.append(e)
    else: m[i]=e
    d.append(i+1)
c=len(m)
print(n-c)
t=[]
for i,e in enumerate(reversed(d)):
    if(c==e): c-=1
    else: t.append(l[n-i-1][0])
for e in sorted(t): print(e)