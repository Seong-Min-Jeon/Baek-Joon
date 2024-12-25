for i in range(int(input())):
    a,s=int(input()),0
    l,t=list(map(int,input().split())),[0 for _ in range(6)]
    c=1
    while True:
        s=0
        for e in l:
            s+=e        
        if(a<s):
            break
        c+=1
        for i in range(6):
            t[i]=l[i]+l[(i+1)%6]+l[(i-1)%6]+l[(i+3)%6]
        l=t.copy()     
    print(c)