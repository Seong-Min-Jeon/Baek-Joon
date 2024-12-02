a,b=map(int,input().split())
c=0
l=list(i for i in range(2,a+1))
while len(l)>0:
    m=min(l)
    for e in l:
        if(e%m==0):
            c+=1
            l.remove(e)
            if(c==b):
                print(e)