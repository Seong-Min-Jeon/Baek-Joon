import copy
l=[list(map(int,input().split())) for _ in range(5)]
x,y=map(int,input().split())
q=[(x,y,0,0,copy.deepcopy(l))]
while q:
    x,y,c,d,t=q.pop(0)
    if(c>=2): print(1); exit()
    t[x][y]=-1
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=i+x<5 and 0<=j+y<5 and t[x+i][y+j]!=-1):
            if(t[x+i][y+j]==1): q.append((x+i,y+j,c+1,d+1,copy.deepcopy(t)))
            elif(d<2): q.append((x+i,y+j,c,d+1,copy.deepcopy(t)))
print(0)