for _ in range(int(input())):
    m,s=0,0
    t=input().strip()
    for e in t:
        if(e=='['): s+=1
        else: s-=1
        m=max(m,s)
    print(2**(m))