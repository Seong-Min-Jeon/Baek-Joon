import math
n=int(input())
l=[*map(int,input().split())]
r=1
for e in l:
    if(r%e!=0): r*=e//math.gcd(r,e)
print(r*min(l) if r in set(l) else r)