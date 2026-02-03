from bisect import bisect_left as B
I=input; I()
l=[*map(int,input().split())]
m=[]
for e in l:
    i=B(m,e)
    if(i>=len(m)): m.append(e)
    else: m[i]=e
print(len(l)-len(m))