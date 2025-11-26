n=int(input())
l=[*map(int,input().split())]
y,m=0,0
for e in l:
    y+=(e//30+1)*10
    m+=(e//60+1)*15
if(y>m):
    print('M',m)
elif(y<m):
    print('Y',y)
else:
    print('Y M',y)