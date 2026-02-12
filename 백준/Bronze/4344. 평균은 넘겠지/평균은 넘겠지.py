I=input
for _ in range(int(I())):
    l=[*map(int,I().split())]
    n=l.pop(0)
    m=sum(l)/n
    c=0
    for e in l:
        if(e>m): c+=1
    t=str(round(c/n*100,3))
    f=len(t.split('.')[1])
    if(f==1): t+='00'
    elif(f==2): t+='0'
    print(f'{t}%')