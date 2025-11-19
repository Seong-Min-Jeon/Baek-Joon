import sys,math
I=sys.stdin.readline
def ccw(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
n=int(I())
l=[]
x,y=0,0
for _ in range(n):
    a,b,c=I().strip().split()
    a,b=int(a),int(b)
    if(c=='Y'): l.append((a,b)); x+=a; y+=b
print(len(l))
x/=len(l); y/=len(l)
l=sorted(l,key=lambda p:(math.atan2(p[1]-y,p[0]-x),(p[0]-x)**2+(p[1]-y)**2))
t=l.index(min(l))
l=l[t:]+l[:t]
for e in l:
    print(*e)