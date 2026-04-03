import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,k=F()
l=[list(F()) for _ in range(n)]
r=[[0]*n for _ in range(k+1)]
for i in range(n):
    a,b,c,d=l[i]
    for j in range(k,a-1,-1):
        t=r[j-a][i-1]
        r[j][i]=max(r[j][i],t+b if t!=0 or i==0 else 0)
    for j in range(k,c-1,-1):
        t=r[j-c][i-1]
        r[j][i]=max(r[j][i],t+d if t!=0 or i==0 else 0)
print(r[-1][-1])