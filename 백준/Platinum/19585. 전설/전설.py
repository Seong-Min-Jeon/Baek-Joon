import sys
I=sys.stdin.readline
c,n=map(int,I().split())
a,b=set([I().strip() for _ in range(c)]),set([I().strip() for _ in range(n)])
for _ in range(int(I())):
    s=I().strip()
    f=1
    x,y='',s
    for i in range(min(1000,len(s))):
        x+=s[i]
        y=s[i+1:]
        if(x in a and y in b): print('Yes'); f=0; break
    if(f): print('No')