import sys,math
I=sys.stdin.readline
def ccw(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
g=0
while True:
    g+=1
    n=int(I())
    if(n==0): break
    z=1e99
    l=[tuple(map(int,I().split())) for _ in range(n)]
    l.sort(key=lambda x:(x[1],x[0]))
    v=l[0]
    l=[v]+sorted(l[1:],key=lambda p:(math.atan2(p[1]-v[1],p[0]-v[0]),(p[0]-v[0])**2+(p[1]-v[1])**2))
    r=[]
    for p in l:
        while len(r)>=2 and ccw(r[-2][0],r[-2][1],r[-1][0],r[-1][1],p[0],p[1])<=0:
            r.pop()
        r.append(p)
    r.append(r[0])
    for i in range(len(r)-1):
        t=0
        a,b=r[i]
        c,d=r[i+1]
        if(a==c):
            for x,y in r:
                t=max(t,abs(x-a))
            z=min(z,t)
            continue
        m=(b-d)/(a-c)
        k=b-m*a        
        for x,y in r:
            t=max(t,abs(m*x-y+k)/(m**2+1)**0.5)
        z=min(z,t)
    u=1e-9
    t=str(math.ceil(z*100-u)/100)
    if(len(t.split('.')[1])==1): t+='0'
    elif(len(t.split('.')[1])==0): t+='00'
    print(f'Case {g}: {t}')