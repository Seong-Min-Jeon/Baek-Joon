import sys
ip=sys.stdin.readline
l=[0 for _ in range(1000001)]
l[0],l[1]=1,1
for i in range(2,int(1000000**0.5+1)):
    for j in range(i*2,1000001,i):
        l[j]=1
p=[]
for i in range(len(l)):
    if(l[i]==0):
        p.append(i)
s=set(p)
for _ in range(int(ip())):
    a=int(ip())
    c=0
    for e in p:
        if(e>=a): break
        if(a-e in s):
            if(a==2*e):
                c+=1
            else: c+=0.5
    print(int(c))