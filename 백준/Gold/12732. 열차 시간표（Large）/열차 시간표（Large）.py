import sys
import heapq
I=sys.stdin.readline
for n in range(int(I())):
    t=int(I())
    a,b=map(int,I().split())
    x=[]
    for _ in range(a):
        s,d=I().split()
        i,j=int(s.split(":")[0]),int(s.split(":")[1])
        k,l=int(d.split(":")[0]),int(d.split(":")[1])+t
        x.append([i*60+j,k*60+l,0])
    for _ in range(b):
        s,d=I().split()
        i,j=int(s.split(":")[0]),int(s.split(":")[1])
        k,l=int(d.split(":")[0]),int(d.split(":")[1])+t
        x.append([i*60+j,k*60+l,1])
    heapq.heapify(x)
    a,b=[],[]
    p,q=0,0
    while x:
        s,d,f=heapq.heappop(x)
        if(f==0 and len(b)>0 and s>=b[0]): heapq.heappop(b); heapq.heappush(a,d)
        elif(f==1 and len(a)>0 and s>=a[0]): heapq.heappop(a); heapq.heappush(b,d)
        elif(f==0): p+=1; heapq.heappush(a,d)
        else: q+=1; heapq.heappush(b,d)
    print(f'Case #{n+1}: {p} {q}')