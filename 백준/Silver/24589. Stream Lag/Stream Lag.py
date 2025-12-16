import sys
I=sys.stdin.readline
c=0
for _ in range(int(I())):
    a,b=map(int,I().split())
    c=max(c,a-b)
print(c)