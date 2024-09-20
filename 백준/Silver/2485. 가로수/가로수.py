import sys
import math
ip=sys.stdin.readline
l=[]
for _ in range(int(ip())):
    l.append(int(ip()))
m=set()
for i in range(len(l)-1):
    m.add(l[i+1]-l[i])
n=math.gcd(*m)
r=1+(max(l)-min(l))//n
print(r-len(l))