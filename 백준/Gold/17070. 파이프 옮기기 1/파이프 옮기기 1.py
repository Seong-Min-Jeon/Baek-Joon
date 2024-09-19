def move(y,x,s):
    if(l[y][x]==1): return
    if(s=='d'):
        if(l[y-1][x]==1): return
        if(l[y][x-1]==1): return
    if(x==n-1 and y==n-1):
        r[0]+=1
    if(s=='g'):
        if(x+1<n):
            move(y,x+1,'g')
        if(x+1<n and y+1<n):
            move(y+1,x+1,'d')
    elif(s=='s'):
        if(y+1<n):
            move(y+1,x,'s')
        if(x+1<n and y+1<n):
            move(y+1,x+1,'d')
    else:
        if(x+1<n):
            move(y,x+1,'g')
        if(y+1<n):
            move(y+1,x,'s')
        if(x+1<n and y+1<n):
            move(y+1,x+1,'d')

n=int(input())
if(n==1): print(0); exit()
l=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    p=input()
    if('1' in p):
        q=list(map(int,p.split()))
        for j in range(n):
            if(q[j]==1):
                l[i][j]=1
r=dict()
r[0]=0
move(0,1,'g')
print(r[0])