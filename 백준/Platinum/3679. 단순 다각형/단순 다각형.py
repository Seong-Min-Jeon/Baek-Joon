import sys,math
I=sys.stdin.readline
for _ in range(int(I())):
    l=[]
    t=[*map(int,I().split())]
    x,y=0,0
    for i in range(t[0]):
        a,b=t[2*i+1],t[2*i+2]
        x+=a;y+=b
        l.append((a,b,i))
    x/=t[0]; y/=t[0]
    l.sort(key=lambda x:(x[1],x[0]))
    v=l[0]
    l=sorted(l,key=lambda p:(math.atan2(p[1]-y,p[0]-x),(p[0]-x)**2+(p[1]-y)**2))
    print(*[e[-1] for e in l])