def f(n,s,c):
    if(n==1 or n==4 or n==8): return 'm'
    elif(n<=10): return 'o'
    a=(s-c)//2
    if(n<a): return f(n,a,c-1)
    elif(a<n<=a+c):
        if(n-a==1): return 'm'
        else: return 'o'
    else: return f(n-a-c,a,c-1)
print(f(int(input()),1073741792,30))