import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    n,m=map(int,ip().split())
    l=list(map(int,ip().split()))
    p=0
    while len(l)>0:
        if(l[0] != max(l)):
            l.append(l[0])
            del l[0]
            if(m==0):
                m=len(l)-1
            else:
                m-=1
        else:
            p+=1
            if(m==0):
                print(p)
                break
            del l[0]
            m-=1