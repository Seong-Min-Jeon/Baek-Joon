from bisect import bisect_left as b
input()
l=list(map(int,input().split()))
m=[]
for e in l:
    i=b(m,e)
    if(i>=len(m)): m.append(e)
    else: m[i]=e
print(len(m))