while True:
    a=input()
    if(a=='0'): break
    p=1
    for i in range(len(a)//2):
        if(a[i]!=a[len(a)-1-i]): p=0
    if(p): print('yes')
    else: print('no')