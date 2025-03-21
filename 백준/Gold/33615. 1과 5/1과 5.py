import sys
I=sys.stdin.readline
for _ in range(int(I())):
    c=0
    s=I().strip()
    t=int(s)
    j=2
    for j in range(2,20):
        if(t%j==0 and t!=j): t//=j; print(0,j); c=1; break
    if(c): continue
    for i in range(len(s)):
        if(i>0 and s[i]==s[i-1]): continue
        if(c): break
        t=int(s[:i]+s[i+1:])
        for j in range(2,20):
            if(t%j==0 and t!=j): t//=j; print(i+1,j); c=1; break