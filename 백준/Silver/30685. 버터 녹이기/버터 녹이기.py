import sys
I=sys.stdin.readline
n=int(input())
l=[tuple(map(int,I().split())) for _ in range(n)]
l.sort()
m=1e9
for i in range(n-1):
    t=0
    x,y=l[i][0],l[i+1][0]
    a=min(l[i][1],l[i+1][1])//2
    if(x+l[i][1]//2<y-l[i+1][1]//2): continue
    if(x+a+1<y-a):
        t+=min(l[i][1],l[i+1][1])//2
        x+=a; y-=a
        t+=y-x-1
    else:
        t=(y-x-1)//2
    m=min(m,t)
if(m==1e9): print('forever')
else: print(m)