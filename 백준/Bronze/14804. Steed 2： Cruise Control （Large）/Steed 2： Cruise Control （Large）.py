import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
for i in range(int(I())):
    k,n=F()
    l=[]
    for _ in range(n):
        a,b=F()
        l.append((k-a)/b)
    m=1e99
    for e in l:
        m=min(m,k/e)
    print(f'Case #{i+1}: {m}')