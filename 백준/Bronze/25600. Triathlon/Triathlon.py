import sys
i=sys.stdin.readline
m=0
for _ in range(int(i())):
    a,b,c=map(int,input().split())
    if(a==b+c): m=max(m,a**2*2)
    else: m=max(m,a*(b+c))
print(m)