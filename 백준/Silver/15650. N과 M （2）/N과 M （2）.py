def f(x):
    if(len(l)==m):
        for e in l:
            print(e,end=' ')
        print()
        return
    for i in range(x,n+1):
        if(i not in l):
            l.append(i)
            f(i)
            l.pop()

n,m=map(int,input().split())
l=[]
f(1)