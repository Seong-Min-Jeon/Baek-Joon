import sys
a=int(input())
l=[]
for _ in range(a):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in l:
    print(i)