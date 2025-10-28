I=input
F=lambda:map(int,I().split())
n,m=F()
t=[sum(c) for c in zip(*[F() for _ in range(n)])]
w=int(I())
r=0
for i in range(m-w+1):
    r=max(r,sum(t[i:w+i]))
print(r)