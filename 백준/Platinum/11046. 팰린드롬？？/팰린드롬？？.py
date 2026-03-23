def manacher(s):
    n=len(s)
    d1=[0]*n
    l=r=-1
    for i in range(n):
        k=1 if i>r else min(d1[l+r-i],r-i+1)
        while i-k>=0 and i+k<n and s[i-k]==s[i+k]: k+=1
        d1[i]=k
        k-=1
        if i+k>r:
            l=i-k
            r=i+k
    d2=[0]*n
    l=r=-1
    for i in range(n):
        k=0 if i>r else min(d2[l+r-i+1],r-i+1)
        while i-k-1>=0 and i+k<n and s[i-k-1]==s[i+k]: k+=1
        d2[i]=k
        k-=1
        if i+k>r:
            l=i-k-1
            r=i+k
    return d1,d2

import sys
I=sys.stdin.readline
I()
s=['#']+[*map(int,I().split())]
d1,d2=manacher(s)
for _ in range(int(I())):
    a,b=map(int,I().split())
    if((b-a)%2):
        c=(a+b)//2+1
        if(d2[c]*2>=b-a+1): print(1)
        else: print(0)
    else:
        c=(a+b)//2
        if(d1[c]*2-1>=b-a+1): print(1)
        else: print(0)