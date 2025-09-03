import sys
I=sys.stdin.readline; I()
l=[0]
for e in map(int,I().split()): l.append(l[-1]+e)
for _ in range(int(I())):
    i,j=map(int,I().split())
    print(l[j]-l[i-1])