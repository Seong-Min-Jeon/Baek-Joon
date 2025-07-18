n,m=map(int,input().split())
t=[*map(int,input().split())]
p=[t[i]-m for i in range(n)]
v=set(t)
c,r,j=0,0,0
for i in range(10**6+9):
    if(r<0): print('fail'); break
    if(j>=n): print('success'); break    
    if(i in v): r-=1
    elif(p[j]<=i<t[j] and c>0): c-=1; r+=1; j+=1
    else: c+=1