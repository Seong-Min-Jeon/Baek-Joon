import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,k=F()
l=[]
for i in range(k):
    a,b=F()
    l.append((a,i+1))
    l.append((b,i+1))
l.sort()
print(l[(n-1)%(2*k)][1])