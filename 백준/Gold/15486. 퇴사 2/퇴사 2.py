import sys
I=sys.stdin.readline
n=int(I())
l=[tuple(map(int,I().split())) for _ in range(n)]
d=[0]*(n+50)
for i in range(n):
    d[i+l[i][0]]=max(d[i+l[i][0]],d[i]+l[i][1])
    d[i+1]=max(d[i+1],d[i])
print(max(d[:n+1]))