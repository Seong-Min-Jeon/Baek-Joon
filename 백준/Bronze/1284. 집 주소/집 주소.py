while True:
    n=int(input())
    if(n==0): break
    l=[0]*10
    for e in str(n): l[int(e)]+=1
    r=l[0]*4
    r+=l[1]*2
    r+=(sum(l)-l[0]-l[1])*3
    print(r+sum(l)+1)