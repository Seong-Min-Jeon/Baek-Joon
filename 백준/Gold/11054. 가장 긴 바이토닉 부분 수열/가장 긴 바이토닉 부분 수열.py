a=int(input())
l=list(map(int,input().split()))
m=l[::-1]
r=[0 for _ in range(a)]
s=[0 for _ in range(a)]
for i in range(a):
    r[i]=1
    s[i]=1
    for j in range(i):
        if(l[i]>l[j]):
            r[i]=max(r[i],r[j]+1)
        if(m[i]>m[j]):
            s[i]=max(s[i],s[j]+1)
s.reverse()
x=0
for i in range(a):
    x=max(x,r[i]+s[i]-1)
print(x)