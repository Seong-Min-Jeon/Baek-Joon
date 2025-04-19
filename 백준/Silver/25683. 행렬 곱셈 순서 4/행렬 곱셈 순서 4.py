import sys
I=sys.stdin.readline
l=[tuple(map(int,I().split())) for _ in range(int(I()))]
s=0
a,b=l.pop()
while l:
    x,y=l.pop()
    s+=a*b*x
    a=x
print(s)