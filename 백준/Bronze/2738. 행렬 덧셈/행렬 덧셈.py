n,m=map(int,input().split())
l=[]
for _ in range(2*n):
    for t in map(int,input().split()):
        l.append(t)
for a in range(n):
    for b in range(m):
        print(l[a*m+b]+l[a*m+b+n*m], end=" ")
    print()