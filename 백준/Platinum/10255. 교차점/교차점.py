import sys
I=sys.stdin.readline
def f(t,n,m):
    a,b,x,y=t
    return (a*y+x*m+n*b)-(a*m+x*b+n*y)
for _ in range(int(I())):
    a,b,c,d=map(int,I().split())
    w,x,y,z=map(int,I().split())
    u,i,o,p=(a,b,a,d),(a,b,c,b),(c,b,c,d),(a,d,c,d)
    if((w,x,y,z)==u or (w,x,y,z)==i or (w,x,y,z)==o or (w,x,y,z)==p): print(4); continue
    if((y,z,w,x)==u or (y,z,w,x)==i or (y,z,w,x)==o or (y,z,w,x)==p): print(4); continue
    if(w==y):
        if(w<min(a,c)): print(0); continue
        elif(max(a,c)<w): print(0); continue
        v=0
        if(min(x,z)<=d<=max(x,z)): v+=1
        if(min(x,z)<=b<=max(x,z)): v+=1
        if((w==a or w==c) and (min(x,z)<b<max(x,z) or min(x,z)<d<max(x,z))): print(4); continue
        if((w==a or w==c) and (min(b,d)<x<max(b,d) or min(b,d)<z<max(b,d))): print(4); continue
        else: print(v); continue
    if(x==z):
        if(x<min(b,d)): print(0); continue
        elif(max(b,d)<x): print(0); continue
        v=0
        if(min(w,y)<=c<=max(w,y)): v+=1
        if(min(w,y)<=a<=max(w,y)): v+=1
        if((x==b or x==d) and (min(w,y)<a<max(w,y) or min(w,y)<c<max(w,y))): print(4); continue
        if((x==b or x==d) and (min(a,c)<w<max(a,c) or min(a,c)<y<max(a,c))): print(4); continue
        else: print(v); continue
    g=0
    for n in (u,i,o,p):
        if(f(n,w,x)*f(n,y,z)<=0 and f((w,x,y,z),n[0],n[1])*f((w,x,y,z),n[2],n[3])<=0):
            if(f((w,x,y,z),n[0],n[1])==0):
                s=(z-x)/(y-w)
                if(s<0 and n[0]==a and n[1]==b): print(1); g=-1; break
                elif(s<0 and n[0]==c and n[1]==d): print(1); g=-1; break
                elif(s>0 and n[0]==a and n[1]==d): print(1); g=-1; break
                elif(s>0 and n[0]==c and n[1]==b): print(1); g=-1; break
                elif(s>0 and n[0]==a and n[1]==b and max(w,y)<max(a,c) and max(x,z)<max(b,d)): print(1); g=-1; break
                elif(s>0 and n[0]==c and n[1]==d and min(w,y)>min(a,c) and min(x,z)>min(b,d)): print(1); g=-1; break
                elif(s<0 and n[0]==a and n[1]==d and max(w,y)<max(a,c) and min(x,z)>min(b,d)): print(1); g=-1; break
                elif(s<0 and n[0]==c and n[1]==b and min(w,y)>min(a,c) and max(x,z)<max(b,d)): print(1); g=-1; break
            elif(f((w,x,y,z),n[2],n[3])==0):
                s=(z-x)/(y-w)
                if(s<0 and n[2]==a and n[3]==b): print(1); g=-1; break
                elif(s<0 and n[2]==c and n[3]==d): print(1); g=-1; break
                elif(s>0 and n[2]==a and n[3]==d): print(1); g=-1; break
                elif(s>0 and n[2]==c and n[3]==b): print(1); g=-1; break
                elif(s>0 and n[2]==a and n[3]==b and max(w,y)<max(a,c) and max(x,z)<max(b,d)): print(1); g=-1; break
                elif(s>0 and n[2]==c and n[3]==d and min(w,y)>min(a,c) and min(x,z)>min(b,d)): print(1); g=-1; break
                elif(s<0 and n[2]==a and n[3]==d and max(w,y)<max(a,c) and min(x,z)>min(b,d)): print(1); g=-1; break
                elif(s<0 and n[2]==c and n[3]==b and min(w,y)>min(a,c) and max(x,z)<max(b,d)): print(1); g=-1; break
            for m in (u,i,o,p):
                if(n==m): continue
                if(f(m,w,x)*f(m,y,z)<=0 and f((w,x,y,z),m[0],m[1])*f((w,x,y,z),m[2],m[3])<=0):
                    g=max(g,2)
                g=max(g,1)
    if(g>=0): print(g)