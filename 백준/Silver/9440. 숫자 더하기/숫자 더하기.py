while True:
    t=input()
    if(t=='0'): break
    l=list(map(int,t.split()))
    n=l.pop(0)
    l.sort()
    a,b=0,0
    for e in l.copy():
        if(a!=0 and b!=0): break
        if(e!=0 and a==0): l.remove(e); a=e
        elif(e!=0 and b==0): l.remove(e); b=e
    for i in range(n-2):
        if(i%2==0): a=a*10+l[i]
        else: b=b*10+l[i]
    print(a+b)