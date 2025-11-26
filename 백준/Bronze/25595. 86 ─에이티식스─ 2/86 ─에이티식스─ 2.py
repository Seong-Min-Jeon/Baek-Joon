n=int(input())
l=[[*map(int,input().split())] for _ in range(n)]
s,a,b=0,0,0
for i in range(n):
    for j in range(n):
        if(l[i][j]==2):
            s=(i+j)%2
        elif(l[i][j]==1):
            a+=(i+j)%2==0
            b+=(i+j)%2==1
if(s and b): print('Kiriya')
elif(not s and a): print('Kiriya')
else: print('Lena')