import sys
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,k=f()
w,v=[0],[0]
for _ in range(n):
    a,b=f()
    w.append(a)
    v.append(b)
l=[[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if(w[i]<=j): l[i][j]=max(l[i-1][j],l[i-1][j-w[i]]+v[i])
        else: l[i][j]=l[i-1][j]
print(l[-1][-1])