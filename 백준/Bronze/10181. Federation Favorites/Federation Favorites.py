while True:
    a,b=int(input()),0
    if(a==-1): break
    l=[]
    for i in range(1,a):
        if(a%i==0): l.append(i); b+=i
    if(a!=b): print(f'{a} is NOT perfect.')
    else:
        c=''
        c+=f'{a} = '
        for i in l:
            c+=f'{i} + '
        print(c[0:len(c)-3])