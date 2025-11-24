import math
I=input
F=lambda:map(int,I().split())
n,r=F()
l=[]
p=[*F()]
s=p
for _ in range(n-1):
    q=[*F()]
    l.append(math.dist(p,q))
    p=q.copy()
l.append(math.dist(s,p))
z=0
for d in l:
    z+=2/3*math.pi*(r-d/2)**2*(2*r+d/2) if d<2*r else 0
print(4*math.pi*r**3/3*n-z)