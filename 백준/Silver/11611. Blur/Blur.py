import copy
w,h,b=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if(l[i][j]==1):
            l[i][j]=9**9
for k in range(b):
    t=copy.deepcopy(l)
    for i in range(h):
        for j in range(w):
            s=l[i][j]+l[i][j-1]+l[i-1][j-1]+l[i-1][j]
            if(i+1==h): s+=l[0][j]+l[0][j-1]
            else: s+=l[i+1][j]+l[i+1][j-1]
            if(i+1==h and j+1==w): s+=l[0][0]
            elif(i+1==h): s+=l[0][j+1]
            elif(j+1==w): s+=l[i+1][0]
            else: s+=l[i+1][j+1]
            if(j+1==w): s+=l[i][0]+l[i-1][0]
            else: s+=l[i][j+1]+l[i-1][j+1]
            t[i][j]=s//9
    l=copy.deepcopy(t)
s=set()
for i in range(h):
    for j in range(w):
        s.add(l[i][j])
print(len(s))