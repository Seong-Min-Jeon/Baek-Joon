import sys,math
I=sys.stdin.readline
def ccw(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
n=int(I())
l=[tuple(map(int,I().split())) for _ in range(n)]
l.sort(key=lambda x:(x[1],x[0]))
v=l[0]
l=[v]+sorted(l[1:],key=lambda p:(math.atan2(p[1]-v[1],p[0]-v[0]),(p[0]-v[0])**2+(p[1]-v[1])**2))
r=[]
for p in l:
    while len(r)>=2 and ccw(r[-2][0],r[-2][1],r[-1][0],r[-1][1],p[0],p[1])<=0:
        r.pop()
    r.append(p)
print(len(r))