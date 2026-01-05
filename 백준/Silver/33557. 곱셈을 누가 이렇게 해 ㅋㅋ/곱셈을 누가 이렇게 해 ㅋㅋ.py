for _ in range(int(input())):
    a,b=map(int,input().split())
    s=''
    for i in range(min(len(str(a)),len(str(b)))):
        s=str(int(str(a)[-1-i])*int(str(b)[-1-i]))+s
    a,b=max(a,b),min(a,b)
    for i in range(len(str(a))-len(str(b))-1,-1,-1):
        s=str(a)[i]+s
    print(1 if a*b==int(s) else 0)