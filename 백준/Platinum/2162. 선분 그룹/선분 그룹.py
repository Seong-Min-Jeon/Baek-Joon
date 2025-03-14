import sys
I=sys.stdin.readline
def f(a,b,c,d,x,y): return (a*d+c*y+x*b)-(c*b+x*d+a*y)
n=int(I())
l=[[] for _ in range(n)]
for _ in range(n):
    a,b,c,d=map(int,I().split())
    k=1
    for t in l:
        if(len(t)==0 and k): t.append((a,b,c,d)); break
        for v,w,x,y in t.copy():
            if(f(a,b,c,d,v,w)==f(a,b,c,d,x,y)==f(v,w,x,y,a,b)==f(v,w,x,y,c,d)==0):
                if((min(v,x)<=a<=max(v,x) and min(w,y)<=b<=max(w,y)) or (min(a,c)<=v<=max(a,c) and min(b,d)<=w<=max(b,d))):
                    t.append((a,b,c,d))
                    k=0
                    break
                else: pass
            elif(f(a,b,c,d,v,w)*f(a,b,c,d,x,y)<=0 and f(v,w,x,y,a,b)*f(v,w,x,y,c,d)<=0):
                t.append((a,b,c,d))
                k=0
                break
t=[]
for i in range(len(l)):
    if(len(l[i])!=0): t.append(set(l[i]))
f=1
while f:
    f=0
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if(len(t[i].intersection(t[j]))!=0):
                t[i]=t[i].union(t[j])
                t[j].clear()
                f=1
n,m=0,0
for i in range(len(t)):
    if(len(t[i])!=0):
        n+=1
        m=max(m,len(t[i]))
print(n)
print(m)