import sys
ip=sys.stdin.readline
l=[[0 for _ in range(15)] for _ in range(15)]
for i in range(15):
    for j in range(15):
        if(i==0): l[i][j]=j
        elif(j<=1): l[i][j]=j
        else: l[i][j]=l[i-1][j]+l[i][j-1]
for _ in range(int(ip())):
    k=int(ip())
    n=int(ip())
    print(l[k][n])