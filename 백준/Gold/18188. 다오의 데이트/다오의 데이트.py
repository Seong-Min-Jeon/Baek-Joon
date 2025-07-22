def f(t,x,y):
 if(t in s and 0<=x<h and 0<=y<w and  l[x][y]!='@'):q.append((x,y,z+t))
I=input;h,w=map(int,I().split())
l=[list(I().strip()) for _ in range(h)]
n=int(I())
c=[I().split() for _ in range(n)]
s,g,q=0,0,0
for i in range(h):
 for j in range(w):
  if(l[i][j]=='D'):s=(i,j,'');q=[s]
  if(l[i][j]=='Z'):g=(i,j)
while q:
 x,y,z=q.pop(0)
 if((x,y)==g): print(f'YES\n{z}'); exit()
 if(len(z)>=n): continue
 s=c[len(z)]
 f('W',x-1,y);f('S',x+1,y);f('A',x,y-1);f('D',x,y+1)
print('NO')