from bisect import bisect_left as b
n=int(input())
l=list(map(int,input().split()))
m=[]
for e in l:
    i=b(m,e)
    if(len(m)<=i): m.append(e)
    else: m[i]=e
print(n-len(m))