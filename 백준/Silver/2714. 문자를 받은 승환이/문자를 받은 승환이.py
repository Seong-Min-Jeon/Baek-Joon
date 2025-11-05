for _ in range(int(input())):
    r,c,m=input().strip().split()
    r,c=int(r),int(c)
    l,t=[],[]
    f=0
    for e in m:
        if(f<c):
            t.append(e)
            f+=1
        if(f>=c):
            l.append(t)
            t=[]
            f=0
    z={}
    for i in range(1,27):
        z[str(bin(i))[2:].rjust(5,'0')]=chr(64+i)
    v=[[0]*c for _ in range(r)]
    x,y,d=0,0,0
    t=''
    w=''
    for _ in range(r*c):
        v[x][y]=1
        t+=l[x][y]
        if(len(t)==5):
            if(t!='00000'): w+=z[t]
            else: w+=' '
            t=''
        if(d==0 and (y+1>=c or v[x][y+1]==1)):
            x,d=x+1,1
        elif(d==0):
            y+=1
        elif(d==1 and (x+1>=r or v[x+1][y]==1)):
            y,d=y-1,2
        elif(d==1):
            x+=1
        elif(d==2 and (y-1<0 or v[x][y-1]==1)):
            x,d=x-1,3
        elif(d==2):
            y-=1
        elif(d==3 and (x-1<0 or v[x-1][y]==1)):
            y,d=y+1,0
        elif(d==3):
            x-=1
    print(w.rstrip())