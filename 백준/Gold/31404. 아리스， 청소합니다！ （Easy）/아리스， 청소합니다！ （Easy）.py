import sys
I=sys.stdin.readline
h,w=map(int,I().split())
r,c,d=map(int,I().split())
o=[list(map(int,list(I().strip()))) for _ in range(h)]
t=[list(map(int,list(I().strip()))) for _ in range(h)]
m=[[0]*w for _ in range(h)]
s=0
p=0
while True:
    n=0
    f=1
    while True:
        if(not p and m[r][c]==0): 
            m[r][c]=1
            n+=1
            f=0
            d+=o[r][c]
            d%=4
        elif(not p and m[r][c]==1):
            p=1
            break
        elif(p and m[r][c]==1):
            n+=1
            d+=t[r][c]
            d%=4
        elif(p and m[r][c]==0):
            p=0
            f=0
            break
        if(d==0): r-=1
        elif(d==1): c+=1
        elif(d==2): r+=1
        else: c-=1
        if(not(0<=r<h and 0<=c<w)):
            if(not p): s+=n
            f=1
            break
        if(n>2**14): break
    if(f): break
    s+=n
print(s)