import sys
i=sys.stdin.readline
a=int(i())
l=set(map(int,i().split()))
c=int(i())
m=list(map(int,i().split()))
n=[0]*c
for i in range(len(m)):
    if(l.issuperset([m[i]])): n[i]=1
    else: n[i]=0
s=''
for i in n:
    print(i, end=' ')