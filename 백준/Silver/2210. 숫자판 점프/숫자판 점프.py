l=[list(map(int,input().split())) for _ in range(5)]
s=set()
for i in range(5):
    for j in range(5):
        q=[(i,j,'')]
        while q:
            i,j,k=q.pop(0)
            for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                if(0<=x+i<5 and 0<=y+j<5):
                    t=k+str(l[x+i][y+j])
                    if(len(t)==6): s.add(t)
                    else: q.append((x+i,y+j,t))
print(len(s))