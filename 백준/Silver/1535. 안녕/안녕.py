n=int(input())
d=[0]+[*map(int,input().split())]
h=[0]+[*map(int,input().split())]
l=[[0]*(101) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(101):
        if(d[i]<=j): l[i][j]=max(l[i-1][j],l[i-1][j-d[i]]+h[i])
        else: l[i][j]=l[i-1][j]
print(l[n][99])