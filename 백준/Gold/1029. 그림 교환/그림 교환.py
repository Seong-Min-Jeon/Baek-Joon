n=int(input())
l=[[*map(int,list(input().strip()))] for _ in range(n)]
d=[[10**9]*(1<<n) for _ in range(n)]
d[0][1<<0]=0
for b in range(1<<n):
    for i in range(n):
        for j in range(n):        
            if(b&(1<<j)==0 and d[i][b]<=l[i][j]):
                d[j][b|(1<<j)]=min(d[j][b|(1<<j)],l[i][j])
r=0
for j in range(n):
    for k in range(1<<n):
        if(d[j][k]!=10**9):
            r=max(r,bin(k).count('1'))
print(r)