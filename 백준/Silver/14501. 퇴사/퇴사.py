def f(t,p):
    global m
    if(t>n): return
    elif(t==n): m=max(m,p); return
    f(l[t][0]+t,l[t][1]+p)
    f(t+1,p)
n=int(input())
l=[tuple(map(int,input().split())) for _ in range(n)]
m=0
f(0,0)
print(m)