import sys
I=sys.stdin.readline
l=[]
for _ in range(int(I())):
    n,m=map(int,I().split())
    s=set()
    for i in range(n,n+m):
        if(i!=n and i%4==0): break
        s.add(i)
    for i in range(n+m-1,n-1,-1):
        if(i!=n+m-1 and i%4==0): s.add(i); break
        s.add(i)
    t=0
    for e in s:
        t^=e
    l.append(t)
x=0
for e in l: x^=e
print('cubelover' if x==0 else 'koosaga')