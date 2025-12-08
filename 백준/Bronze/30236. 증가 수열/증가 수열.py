I=input
for _ in range(int(I())):
    n=int(I())
    l=[*map(int,I().split())]
    c=0
    for i in range(n):
        if(i+c+1==l[i]):c+=1
    print(n+c)