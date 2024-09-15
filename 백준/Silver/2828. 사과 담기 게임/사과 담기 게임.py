import sys
ip=sys.stdin.readline
a,b=map(int,ip().split())
p=1
c=int(ip())
m=0
for _ in range(c):
    d=int(ip())
    if(p<=d and p+b-1>=d):
        continue
    elif(p<d):
        m+=d-p-b+1
        p=d-b+1
    else:
        m+=p-d
        p=d
print(m)