s=input().strip()
def f(s,p):
    a=s[:len(s)//2+p]
    b=s[len(s)//2+p:]
    l=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if(a[i-1]==b[j-1]): l[i][j]=l[i-1][j-1]+1
            else: l[i][j]=max(l[i-1][j],l[i][j-1])
    return min(len(a),len(b))-max(max(e for e in l))
if(len(s)%2==1): print(max(f(s,0),f(s,1)))
else: print(f(s,0))