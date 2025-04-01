for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        c+=str(i).count('0')
    print(c)