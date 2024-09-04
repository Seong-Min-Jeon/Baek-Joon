import sys
a=int(sys.stdin.readline())
for i in range(a):
    l=list(map(int,sys.stdin.readline().split()))
    l.sort()
    print(l[2]**2+(l[0]+l[1])**2)