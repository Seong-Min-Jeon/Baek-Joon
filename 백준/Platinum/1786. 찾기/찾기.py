def kmp(s,p):
    m=len(p)
    pi=[0]*m
    j=0
    for i in range(1,m):
        while j and p[i]!=p[j]:
            j=pi[j-1]
        if(p[i]==p[j]):
            j+=1
            pi[i]=j
    j=0
    r=[]
    for i in range(len(s)):
        while j and s[i]!=p[j]:
            j=pi[j-1]
        if(s[i]==p[j]):
            if j==m-1:
                r.append(i-m+2)
                j=pi[j]
            else:
                j+=1
    return r

a,b=input().rstrip(),input().rstrip()
l=kmp(a,b)
print(len(l))
print(*l)