import sys
a=int(input())
l=[0]*10001
for _ in range(a):
    l[int(sys.stdin.readline())]+=1
for i in range(10001):
    if(l[i]==0): continue
    for _ in range(l[i]):
        print(i)