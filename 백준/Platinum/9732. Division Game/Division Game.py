import sys
I=sys.stdin.readline
l=[0,0]
for i in range(2,10001):
    t=[0]*10001
    n=i
    for j in range(2,int(i**0.5)+1):
        while n%j==0:
            n//=j
            t[j]+=1
    t[n]+=1
    l.append(sum(t[2:]))
for k in range(int(I())):
    n,m=map(int,I().split())
    r=[]
    for _ in range(n):
        t=0
        for e in map(int,I().split()):
            t+=l[e]
        r.append(t)
    x=0
    for e in r:
        x^=e
    if(x): print(f'Case #{k+1}: YES')
    else: print(f'Case #{k+1}: NO')