ip=input
a,b=map(int,ip().split())
w,x,y,z=map(int,ip().split())
r=0
for _ in range(a):
    r+=ip().count('P')
if(r!=y*z): print(1)
else: print(0)