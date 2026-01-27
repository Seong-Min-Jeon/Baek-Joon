I=input
n=int(I())
m=n*(n*n+1)//2
f=1
l=[[*map(int,I().split())] for _ in range(n)]
for i in range(n):
    if(sum(l[i])!=m): f=0
    if(sum([l[j][i] for j in range(n)])!=m): f=0
t=0
for i in range(n):
    t+=l[i][i]
if(t!=m): f=0
t=0
for i in range(n):
    t+=l[i][n-i-1]
if(t!=m): f=0
s=set()
for i in range(n):
    for j in range(n):
        if(l[i][j] in s): f=0
        s.add(l[i][j])
print('TRUE' if f else 'FALSE')