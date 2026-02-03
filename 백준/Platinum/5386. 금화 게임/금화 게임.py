I=input
def f(v):
    if(v%2==0 and v!=k): return 1
    return 0
for _ in range(int(I())):
    s,k=map(int,I().split())
    if(s<k): k=1
    if(k%2==1):
        if(s%2==0): print(0)
        else: print(1)
    else:
        r=1
        for e in range(30):
            if(f((s-k**e)%(k+1))==1): print(k**e); r=0; break
        if(r): print(0)