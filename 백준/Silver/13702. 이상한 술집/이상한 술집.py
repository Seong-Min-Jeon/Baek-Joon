import sys
I=sys.stdin.readline
n,k=map(int,I().split())
l=[int(I()) for _ in range(n)]
x,z=1,max(l)
while x<=z:
    y=(x+z)//2
    t=[e//y for e in l]
    if(sum(t)>=k): x=y+1
    else: z=y-1
print(z)