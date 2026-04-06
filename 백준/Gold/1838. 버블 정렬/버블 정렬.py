from bisect import bisect_left as B
n=int(input())
l=[*map(int,input().split())]
k=sorted(l)
r=0
for i,e in enumerate(l):
    j=B(k,e)
    r=max(r,i-j)
print(r)