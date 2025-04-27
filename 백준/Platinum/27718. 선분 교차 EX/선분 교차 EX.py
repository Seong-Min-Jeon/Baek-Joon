import sys
I=sys.stdin.readline
def f(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
n=int(I())
l=[list(map(int,I().split())) for _ in range(n)]
t=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a,b,c,d=l[i]
        w,x,y,z=l[j]
        if((a==w and b==x) or (a==y and b==z) or (c==w and d==x) or (c==y and d==z)): t[i][j]=1
        p,q,r,s=f(a,b,c,d,w,x),f(a,b,c,d,y,z),f(w,x,y,z,a,b),f(w,x,y,z,c,d)
        if(p*q<0 and r*s<0): t[i][j]=2
        elif((p*q<0 and r*s==0) or (p*q==0 and r*s<0)): t[i][j]=1
        elif(p==q==r==s==0):
            if((min(a,c)<=w<=max(a,c) and min(b,d)<=x<=max(b,d)) or
               (min(a,c)<=y<=max(a,c) and min(b,d)<=z<=max(b,d)) or
               (min(w,y)<=a<=max(w,y) and min(x,z)<=b<=max(x,z)) or
               (min(w,y)<=c<=max(w,y) and min(x,z)<=d<=max(x,z))): t[i][j]=3
            if(abs(a-c)+abs(b-d)+abs(w-y)+abs(x-z)==max(a,c,w,y)-min(a,c,w,y)+max(b,d,x,z)-min(b,d,x,z)): t[i][j]=1
for e in t:
    print(''.join(list(map(str,e))))