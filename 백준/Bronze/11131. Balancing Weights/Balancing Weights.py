for _ in range(int(input())):
    input()
    s=sum(list(map(int,input().split())))
    if(s>0): print('Right')
    elif(s==0): print('Equilibrium')
    else: print('Left')