import math
n,m=map(int,input().split())
l=[[1 for _ in range(m)] for _ in range(n)]
for i in range(1,n):
    for j in range(m):
        if(j==0): l[i][j]=l[i-1][j]*i
        else: l[i][j]=l[i-1][j-1]+i*l[i-1][j]
a,b=l[-1][-1],math.factorial(n)
g=math.gcd(a,b)
print(f'{a//g}/{b//g}')