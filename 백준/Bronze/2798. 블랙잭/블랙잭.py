a,b=map(int,input().split())
l=list(map(int,input().split()))
a,t,c=300000,0,0
for i in l:
    for j in l:
        if(i==j): continue
        for k in l:
            if(i==k or j==k): continue
            t=i+j+k
            if(a>b-t and b>=t): 
                c=i+j+k
                a=b-c
print(c)                                    