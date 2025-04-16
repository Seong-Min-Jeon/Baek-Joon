import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[list(map(int,I().split())) for _ in range(m)]
l.sort(key=lambda x: x[1])
x,y=0,0
for c,a,b in l:
    if(a==0):
        if(c==0 and b>=0): print('adios'); exit()
        elif(c==1 and b<=0): print('adios'); exit()
        continue
    if(c==0): x,y=a,max(b+1,y-(a-x))
    else:
        if(y-(a-x)>=b): print('adios'); exit()
        else: x,y=a,y-(a-x)
if(y-(n-x)>0): print('adios')
else: print('stay')