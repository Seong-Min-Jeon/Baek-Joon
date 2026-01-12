n=int(input())
l=[list(input().strip()) for _ in range(n)]
x,y=0,0
for i in range(n):
    c,d=0,0
    for j in range(n):
        if(l[i][j]=='X'):
            if(c>1): x+=1
            c=0
        else: c+=1
        if(l[j][i]=='X'):
            if(d>1): y+=1
            d=0
        else: d+=1
    if(c>1): x+=1
    if(d>1): y+=1
print(x,y)