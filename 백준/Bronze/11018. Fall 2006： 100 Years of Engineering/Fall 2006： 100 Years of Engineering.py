for j in range(int(input())):
    n,m=map(float,input().split())
    d,v=0,0
    l=[tuple(map(float,input().split())) for _ in range(int(n))]
    for e in l:
        m+=e[0]
    for i in range(int(n)):
        a=l[i][2]/m-9.81
        t=l[i][1]
        d+=v*t+(0.5)*a*t**2        
        v+=a*t
        m-=l[i][0]
    print(f'Data Set {j+1}:')
    print(f'{d:.2f}')
    print()