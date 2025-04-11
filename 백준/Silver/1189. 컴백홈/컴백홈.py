r,c,k=map(int,input().split())
l=[[0]*c for _ in range(r)]
for i in range(r):
    for j,p in enumerate(list(input().strip())):
        if(p=='.'): l[i][j]=0
        else: l[i][j]=1
q=[(r-1,0,1,[(r-1,0)])]
m=[]
while q:
    x,y,d,s=q.pop(0)
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        t=s.copy()
        if(0<=x+i<r and 0<=y+j<c and (x+i,y+j) not in t and l[x+i][y+j]!=1):
            t.append((x+i,y+j))
            if(d+1==k and x+i==0 and y+j==c-1):
                if(t not in m): m.append(t)
                continue
            q.append((x+i,y+j,d+1,t))
print(len(m))