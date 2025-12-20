for k in range(int(input())):
    if(k>0): input()
    n=int(input())
    l=[*map(int,input().split())]
    p=int(input())
    r=[int(input()) for _ in range(p)]
    b=[]
    for i in r:
        c=0
        for j in range(0,2*n,2):
            if(l[j]<=i<=l[j+1]): c+=1
        b.append(c)
    print(f'Case #{k+1}: {" ".join(map(str,b))}')