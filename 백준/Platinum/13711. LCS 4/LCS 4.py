from bisect import bisect_left as b
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
f,g={},{}
for i in range(n):
    f[x[i]]=i
    g[y[i]]=i
t=[f[y[i]] for i in range(n)]
d=[]
for n in t:
    i=b(d,n)
    if(len(d)<=i): d.append(n)
    else: d[i]=n
print(len(d))