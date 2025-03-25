import sys
I=sys.stdin.readline
a=int(I())
r,g,b=map(int,I().split())
l=[tuple(map(int,I().split())) for _ in range(a-1)]
m=1e9
for i in range(3):
    r1,g1,b1=r,g,b
    if(i==0): g1,b1=10**5,10**5
    elif(i==1): r1,b1=10**5,10**5
    else: r1,g1=10**5,10**5
    for j in range(a-1):
        x,y,z=l[j]
        x+=min(g1,b1)
        y+=min(r1,b1)
        z+=min(r1,g1)
        r1,g1,b1=x,y,z
    if(i==0): m=min(m,g1,b1)
    elif(i==1): m=min(m,r1,b1)
    else: m=min(m,r1,g1)
print(m)