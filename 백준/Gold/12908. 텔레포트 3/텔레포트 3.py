I=input
t=[tuple(map(int,I().split())) for _ in range(2)]
l=[[1e99]*8 for _ in range(8)]
for i in range(1,4):
    a,b,c,d=map(int,I().split())
    t.append((a,b))
    t.append((c,d))
    l[2*i][2*i+1]=10
    l[2*i+1][2*i]=10
for i in range(8):
    for j in range(8):
        d=abs(t[i][0]-t[j][0])+abs(t[i][1]-t[j][1])
        l[i][j]=min(l[i][j],d)
        l[j][i]=min(l[j][i],d)
for k in range(8):
    for i in range(8):
        for j in range(8):
            l[i][j]=min(l[i][j],l[i][k]+l[k][j])
print(l[0][1])