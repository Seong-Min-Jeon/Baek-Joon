def manacher(s):
    n=len(s)
    d1=[0]*n
    l=r=-1
    for i in range(n):
        k=1 if i>r else min(d1[l+r-i],r-i+1)
        while i-k>=0 and i+k<n and s[i-k]==s[i+k]: k+=1
        d1[i]=k
        k-=1
        if i+k>r:
            l=i-k
            r=i+k
    d2=[0]*n
    l=r=-1
    for i in range(n):
        k=0 if i>r else min(d2[l+r-i+1],r-i+1)
        while i-k-1>=0 and i+k<n and s[i-k-1]==s[i+k]: k+=1
        d2[i]=k
        k-=1
        if i+k>r:
            l=i-k-1
            r=i+k
    return d1,d2

s=input().strip()

d1,d2=manacher(s)
a=max(2*x-1 for x in d1)
b=max(2*x for x in d2)
print(max(a,b))