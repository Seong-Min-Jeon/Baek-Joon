import sys
I=sys.stdin.readline
while True:
    n=int(I())
    if(n==0): break
    l=[0 for _ in range(n)]
    for i in range(n):
        a=int(I())
        l[i]=max(l[i-1]+a,a)
    print(max(l))