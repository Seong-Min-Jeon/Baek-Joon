def f():
    k=int(input())
    c,r=0,set()
    for x in range(-5*10**7,5*10**7):
        if(x+k==0): continue
        t=x**2//(x+k)
        if(x**2%(x+k)==0 and t not in r):
            c+=1;r.add(t)
    print(c,-sum(r))
f()