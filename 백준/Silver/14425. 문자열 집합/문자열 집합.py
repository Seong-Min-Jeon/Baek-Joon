import sys
i=sys.stdin.readline
a,b=map(int,i().split())
l=set()
m=list()
for _ in range(a):
    l.add(i().strip())
for _ in range(b):
    m.append(i().strip())
c=0
for i in m:
    if(l.issuperset([i])):
        c+=1        
print(c)