I=input
h,w=map(int,I().split())
l=[list(I().strip()) for _ in range(h)]
n=int(I())
c=[set(I().strip().split()) for _ in range(n)]
s,g=0,0
for i in range(h):
    for j in range(w):
        if(l[i][j]=='D'): s=(i,j,'')
        if(l[i][j]=='Z'): g=(i,j)
q=[s]
while q:
    x,y,z=q.pop(0)
    if((x,y)==g): print(f'YES\n{z}'); exit()
    if(len(z)>=n): continue
    s=c[len(z)]
    if('W' in s and 0<=x-1<h and l[x-1][y]!='@'): q.append((x-1,y,z+'W'))
    if('S' in s and 0<=x+1<h and l[x+1][y]!='@'): q.append((x+1,y,z+'S'))
    if('A' in s and 0<=y-1<w and l[x][y-1]!='@'): q.append((x,y-1,z+'A'))
    if('D' in s and 0<=y+1<w and l[x][y+1]!='@'): q.append((x,y+1,z+'D'))
print('NO')