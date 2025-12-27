a,b,c=map(int,input().split())
s={(a,0),(0,a),(b,0),(0,b),(c,0),(0,c)}
for i in range(501):
    for j in range(501):
        f=0
        for k in (a,b,c):
            if(i>=k and (i-k,j) not in s): f=1
            if(j>=k and (i,j-k) not in s): f=1
            if(f): break
        if(f): s.add((i,j))
for _ in range(5):
    i,j=map(int,input().split())
    if((i,j) in s): print('A')
    else: print('B')