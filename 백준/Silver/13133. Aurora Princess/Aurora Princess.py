import sys
I=sys.stdin.readline
l=set()
for i in range(int(I())):
    a,b=map(int,I().split())
    if(a!=0 and b!=0):
        l.add((i+1,a,b))
m=int(I())
d=[*map(int,I().split())]
for p in d:
    for i,a,b in l.copy():
        if(i==p or a==p or b==p): l.remove((i,a,b))
print(len(l))