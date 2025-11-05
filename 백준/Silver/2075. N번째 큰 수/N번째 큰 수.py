import sys
I=sys.stdin.readline
n=int(I())
l=[*map(int,input().split())]
for _ in range(n-1):
    l+=[*map(int,input().split())]
    l.sort()
    l=l[n:]
print(l[0])