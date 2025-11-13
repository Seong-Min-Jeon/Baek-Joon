for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(2,65):
        l=[]
        t=n
        while t!=0:
            l.append(t%i)
            t//=i
        f=1        
        for j in range(len(l)//2):
            if(l[j]!=l[-1-j]):
                f=0
                break
        if(f):
            c=1
            break
    if(c): print(1)
    else: print(0)