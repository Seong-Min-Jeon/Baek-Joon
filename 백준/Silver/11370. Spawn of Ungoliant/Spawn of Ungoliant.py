import sys
I=sys.stdin.readline
while True:
    w,h=map(int,I().split())
    if(w==0): break
    l=[list(I().strip()) for _ in range(h)]
    q=[]
    for i in range(h):
        for j in range(w):
            if(l[i][j]=='S'): q.append((i,j))
    while q:
        x,y=q.pop()
        for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
            if(0<=x+i<h and 0<=y+j<w and l[x+i][y+j]=='T'):
                l[x+i][y+j]='S'
                q.append((x+i,y+j))
    for i in range(h):
        print(''.join(l[i]))