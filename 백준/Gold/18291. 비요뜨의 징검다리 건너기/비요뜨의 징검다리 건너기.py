import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n=int(I())
    print(pow(2,n-2,10**9+7) if n>1 else 1)