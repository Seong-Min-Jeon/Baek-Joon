def f(i,j,t):
    if(len(t)==6): s.add(t); return
    for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=x+i<5 and 0<=y+j<5): f(x+i,y+j,t+l[x+i][y+j])
l=[input().split() for _ in range(5)]
s=set()
for i in range(25): f(i//5,i%5,'')
print(len(s))