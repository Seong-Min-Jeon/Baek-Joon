while True:
    a,b=map(int,input().split())
    if(a==b==0): break
    l=[*map(int,input().split())]
    x=0
    for i in range(a):
        for j in range(i+1,a):
            if(l[i]+l[j]<=b): x=max(x,l[i]+l[j])
    print(x if x!=0 else "NONE")