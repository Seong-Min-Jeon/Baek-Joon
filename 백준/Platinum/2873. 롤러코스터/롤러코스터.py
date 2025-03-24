import sys
I=sys.stdin.readline
r,c=map(int,I().split())
l=[list(map(int,I().split())) for _ in range(r)]
if(r%2==1):
    f=0
    i,j=0,0
    while True:
        if(f): j-=1; print('L',end='')
        else: j+=1; print('R',end='')
        if(i==r-1 and j==c-1): break
        if(j==0 or j==c-1): i+=1; print('D',end=''); f=int(bin(f^1),2)
elif(c%2==1):
    f=1
    i,j=0,0
    while True:
        if(f): i+=1; print('D',end='')
        else: i-=1; print('U',end='')
        if(i==r-1 and j==c-1): break
        if(i==0 or i==r-1): j+=1; print('R',end=''); f=int(bin(f^1),2)
else:
    x,y=0,0
    m=10**4
    for i in range(r):
        for j in range(c):
            if((i+j)%2==1 and l[i][j]<m):
                x,y=i,j
                m=l[i][j]
    i,j=0,0
    f,g=1,1
    if(y==c-1):
        while True:
            if(f): i+=1; print('D',end='')
            else: i-=1; print('U',end='')
            if(j==c-2): break
            if(i==0 or i==r-1): j+=1; print('R',end=''); f=int(bin(f^1),2)
            if(j==c-2): break
        while True:
            if(i==x and j+1==y): i+=1; print('D',end=''); continue
            j+=1; print('R',end='')
            if(i==r-1 and j==c-1): break
            i+=1; print('D',end='')
            if(i==r-1 and j==c-1): break
            j-=1; print('L',end='')
            i+=1; print('D',end='')
        exit()
    while True:
        if(j==y):
            j+=1
            print('R',end='')
            if(i==r-1 and j==c-1): exit()
            while True:
                if(f): i+=1; print('D',end='')
                else: i-=1; print('U',end='')
                if(i==r-1 and j==c-1): exit()
                if(i==0 or i==r-1):
                    if(j==y): j+=1; print('R',end='')
                    if(i==r-1 and j==c-1): exit()
                    j+=1; print('R',end='')
                    f=int(bin(f^1),2)
                    if(i==r-1 and j==c-1): exit()
                    break
                if(i==x and j-1==y):
                    if(f): i+=1; print('D',end='')
                    else: i-=1; print('U',end='')
                    if(i==r-1 and j==c-1): exit()
                if(g): j-=1; print('L',end=''); g=int(bin(g^1),2)
                else: j+=1; print('R',end=''); g=int(bin(g^1),2)
                if(i==r-1 and j==c-1): exit()
                if(i==0 or i==r-1):
                    if(j==y): j+=1; print('R',end='')
                    if(i==r-1 and j==c-1): exit()
                    j+=1; print('R',end='')
                    f=int(bin(f^1),2)
                    if(i==r-1 and j==c-1): exit()
                    break
        else:
            if(f): i+=1; print('D',end='')
            else: i-=1; print('U',end='')
            if(i==r-1 and j==c-1): break
            if(i==0 or i==r-1): j+=1; print('R',end=''); f=int(bin(f^1),2)
            if(i==r-1 and j==c-1): break