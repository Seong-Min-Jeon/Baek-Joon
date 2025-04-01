n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
r=[0]*n
for i in range(n):
    for j in range(n):
        if(i==j): continue
        r[i]|=l[i][j]
print(*r)