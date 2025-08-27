from itertools import combinations as c
n=int(input())
l=[tuple(map(int,input().split())) for _ in range(n)]
m=0
for e in list(c(l,3)):
    a,b=e[0]; c,d=e[1]; e,f=e[2]
    m=max(m,0.5*abs(a*d+c*f+e*b-c*b-e*d-a*f))
print(m)