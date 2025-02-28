n=int(input())
l=list(map(int,input().split()))
l.reverse()
r=[]
for i in range(n-1):
    if(len(r)==0): r.append(l[i]); continue
    r.append(((r[i-1]+1)*l[i])%(10**9+7))
print(sum(r)%(10**9+7))