l=[]
for _ in range(int(input())):
    l.append(list(map(int,input().split())))
for m in l:
    c=1
    for n in l:
        if(m[0]<n[0] and m[1]<n[1]): c+=1
    print(c, end=' ')