import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
def f(s):
    global r
    if(len(s)==n+1):
        c=0
        for e in l:
            if(len(e.difference(s))==0):
                c+=1
        r=max(r,c)
        return
    for i in range(max(s)+1,2*n+1):
        f(s.union({i}))
n,m,k=F()
l=[]
for _ in range(m):
    l.append(set(F()))
r=0
f({0})
print(r)