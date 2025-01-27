import heapq as H
import sys
I=sys.stdin.readline
for _ in range(int(I())):
    h,g=[],[]
    n=int(I())
    d=[0 for _ in range(n)]
    for i in range(n):
        t=I().split()
        o,p=t[0],int(t[1])
        if(o=='I'): H.heappush(h,(p,i)); H.heappush(g,(-p,i)); continue
        if(p==1): 
            while g:
                t=H.heappop(g)[1]
                if(d[t]==0): d[t]=1; break
        else:
            while h:
                t=H.heappop(h)[1]
                if(d[t]==0): d[t]=1; break        
    n,m=0,0
    while g:
        n=g[0]
        if(d[n[1]]==0): break
        else: H.heappop(g)
    while h:
        m=h[0]
        if(d[m[1]]==0): break
        else: H.heappop(h)
    if(len(h)==0): print('EMPTY')
    else: print(-n[0],m[0])