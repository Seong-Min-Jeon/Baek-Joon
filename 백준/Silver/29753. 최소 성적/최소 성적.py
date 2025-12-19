n,k=input().strip().split()
k=int(k[0]+k[2:])
d={'A+':450,'A0':400,'B+':350,'B0':300,'C+':250,'C0':200,'D+':150,'D0':100,'F':0}
l,s=0,0
for _ in range(int(n)-1):
    c,g=input().strip().split()
    l+=int(c)
    s+=int(c)*d[g]
m=int(input())
l+=m
r='impossible'
for e in d:
    if(d[e]*m>=k*l-s+l): r=e
print(r)