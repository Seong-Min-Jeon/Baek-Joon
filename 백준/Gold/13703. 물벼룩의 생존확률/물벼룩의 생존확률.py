k,n=map(int,input().split())
l=[[0]*200 for _ in range(n+1)]
l[0][100]=2**n
s=0
for i in range(n+1):
    for j in range(1,199):
        if(j==100-k): s+=l[i][j]; continue
        if(i==n): continue
        l[i+1][j+1]+=l[i][j]//2
        l[i+1][j-1]+=l[i][j]//2
print(2**n-s)