def f(s,n):
    if(n==1): return 1
    a,b=s[:n//2],s[n//2+1:]
    if(a.translate(str.maketrans('10','01'))!=b[::-1]): return 0
    return f(a,n//2) or f(b,n//2)
for _ in range(int(input())):
    s=input().strip()
    if(f(s,len(s))): print('YES')
    else: print('NO')