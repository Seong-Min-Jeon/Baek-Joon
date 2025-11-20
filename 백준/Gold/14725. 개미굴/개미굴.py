import sys
I=sys.stdin.readline
d={}
for _ in range(int(I())):
    n,*l=I().split()
    t=d
    for e in l:
        while True:
            if(e in t):
                t=t[e]
                break
            else:
                t[e]={}
def f(t,n):
    for k in sorted(t):
        print('-'*n+k)
        f(t[k],n+2)        
        t.pop(k)
f(d,0)