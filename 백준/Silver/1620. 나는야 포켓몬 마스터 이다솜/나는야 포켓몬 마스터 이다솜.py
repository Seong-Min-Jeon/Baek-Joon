a,b=map(int,input().split())
m=dict()
n=dict()
l=[]
for i in range(a):
    v=input()
    m[v]=i
    n[i]=v
for _ in range(b):
    l.append(input())
for i in l:    
    if(i.isdigit()): print(n.get(int(i)-1))
    else: print(int(m.get(i))+1)