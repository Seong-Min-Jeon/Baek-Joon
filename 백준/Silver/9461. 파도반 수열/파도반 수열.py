import sys
ip=sys.stdin.readline
l=[1,1,1,2,2]
for i in range(5,101):
    l.append(l[len(l)-1]+l[len(l)-5])
for _ in range(int(ip())):
    print(l[int(ip())-1])