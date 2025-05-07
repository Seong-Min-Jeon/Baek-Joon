from itertools import product as p
for _ in range(int(input())):
    n=int(input())
    l=p([' ','+','-'],repeat=n-1)
    for o in l:
        s=''
        for i in range(n):
            if(i==n-1): s+=str(i+1)
            else: s+=str(i+1)+o[i]
        x=s.replace(' ', '')
        r,v,o=0,0,1
        for c in x:
            if(c=='+'):
                if(o): r+=v; v=0
                else: r-=v; v=0
                o=1
            elif(c=='-'):
                if(o): r+=v; v=0
                else: r-=v; v=0
                o=0
            else: v*=10; v+=int(c)
        if(o): r+=v
        else: r-=v
        if(r==0): print(s)
    print()