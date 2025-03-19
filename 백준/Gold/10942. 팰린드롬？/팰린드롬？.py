import sys
I=sys.stdin.readline
n=int(I())
l=list(map(int,I().split()))
r=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if(l[i]==l[j]):
            r[i][j]=r[i-1][j+1]+1
for _ in range(int(I())):
    a,b=map(int,I().split())
    if(abs(a-b)==abs(r[a-1][b-1]-r[b-1][a-1])): print(1)
    else: print(0)