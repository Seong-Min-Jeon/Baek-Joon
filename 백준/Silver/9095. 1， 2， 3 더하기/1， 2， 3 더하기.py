import sys
ip=sys.stdin.readline
l=[1,2,4,7]
for i in range(4,10):
    l.append(l[i-1]+l[i-2]+l[i-3])
for _ in range(int(ip())):
    print(l[int(ip())-1])