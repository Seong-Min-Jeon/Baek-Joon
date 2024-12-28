import sys
ip=sys.stdin.readline
l=[1,2]
for i in range(2,21): l.append(l[i-1]+l[i-2])
l.reverse()
for i in range(int(ip())):
    a,r=int(ip()),0
    k=[0]
    for n in l:
        if(n<=a): a-=n; k.append(1)
        else: k.append(0)
    for i in range(21):
        if(k[i]==1): r+=l[i]
    print(r)