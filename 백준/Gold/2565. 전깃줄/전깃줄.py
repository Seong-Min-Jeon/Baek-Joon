from bisect import bisect_left
l=[tuple(map(int,input().split())) for _ in range(int(input()))]
l.sort()
b=[e[1] for e in l]
m=[]
for e in b:
    i=bisect_left(m,e)
    if(len(m)<=i): m.append(e)
    else: m[i]=e
print(len(l)-len(m))