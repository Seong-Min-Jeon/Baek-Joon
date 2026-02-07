while True:
    l=[*map(int,input().split())]
    if(len(l)==1): break
    t=[1]
    for i in range(l[0]):
        for j in range(2):
            if(j): t[-1]-=l[2*i+j+1]
            else: t.append(t[-1]*l[2*i+j+1])
    print(t[-1])