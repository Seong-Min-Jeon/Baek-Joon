n=int(input())
l=[*map(int,input().split())]
r=[[-1e99]*n for _ in range(n)]
r[0]=[l[0]]*n
for i in range(n):
    t=[-1e99]*n
    t[-1]=r[i][-1]
    for k in range(n-2,-1,-1):
        t[k]=max(t[k+1],r[i][k])
    for j in range(1,n-i):
        r[i+j][j]=max(r[i+j][j],t[j]+l[i+j])
print(max(r[-1]))