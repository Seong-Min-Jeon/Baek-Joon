import sys
def f(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
def g(p,q):
    a,b,c,d=p
    w,x,y,z=q
    if(f(a,b,c,d,w,x)==0 and f(a,b,c,d,y,z)==0 and f(w,x,y,z,a,b)==0 and f(w,x,y,z,c,d)==0 and
       ((min(a,c)<=w<=max(a,c) and min(b,d)<=x<=max(b,d)) or
        (min(a,c)<=y<=max(a,c) and min(b,d)<=z<=max(b,d)) or
        (min(w,y)<=a<=max(w,y) and min(x,z)<=b<=max(x,z)) or
        (min(w,y)<=c<=max(w,y) and min(x,z)<=d<=max(x,z)))):
        return True
def o(s):
    t=s.split('.')
    if(len(t)==1):
        return int(t[0]+'00')
    a,b=t
    if(len(b)==1): b+='0'
    return int(a+b)
I=sys.stdin.readline
n=int(I())
l=[[] for _ in range(n)]
t=[]
for _ in range(n):
    a,b,c,d=I().strip().split()
    t.append((o(a),o(b),o(c),o(d)))
for i in range(n):
    for j in range(i+1):
        if(g(t[i],t[j])):
            l[j].append(i)
            l[i].append(j)
v=[0]*n
c=0
for i in range(n):
    if(v[i]==0): c+=1
    q=[i]
    while q:
        p=q.pop()
        for j in l[p]:
            if(v[j]==0):
                q.append(j)
                v[j]=1
print(c)