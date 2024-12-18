import sys
ip=sys.stdin.readline
a=int(ip())
l=[[0 for _ in range(a+2)] for _ in range(a)]
for i in range(a):
    if(i==0): l[i][1]=int(ip()); continue
    m=list(map(int,ip().split()))
    for j in range(1,len(m)+1):
        l[i][j]=m[j-1]+max(l[i-1][j], l[i-1][j-1])
print(max(l[-1]))