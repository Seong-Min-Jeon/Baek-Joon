for _ in range(int(input())):
    d,n,s,p=map(int,input().split())
    if(n*s==d+p*n): print('does not matter')
    elif(n*s<d+p*n): print('do not parallelize')
    else: print('parallelize')