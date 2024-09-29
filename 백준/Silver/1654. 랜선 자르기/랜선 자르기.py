import sys
ip=sys.stdin.readline
a,b=map(int,ip().split())
l=[]
for _ in range(a): l.append(int(ip()))
n=[0,max(l),max(l)]
m=n.copy()
while True:
    m=n.copy()
    t=0
    for e in l:
        t+=e//n[1]
    if(t<b): 
        n[2]=n[1]
        n[1]=(n[0]+n[1])//2
    else:
        n[0]=n[1]
        n[1]=(n[1]+n[2])//2
    if(n==m):
        break
print(n[1])