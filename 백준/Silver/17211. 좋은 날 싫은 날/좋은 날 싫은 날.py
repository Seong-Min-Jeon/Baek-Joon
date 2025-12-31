import math
n,k=map(int,input().split())
a,b,c,d=map(float,input().split())
g,s=k==0,k==1
for _ in range(n):
    g,s=g*a+s*c,g*b+s*d
print(math.ceil(g*1000),math.ceil(s*1000))