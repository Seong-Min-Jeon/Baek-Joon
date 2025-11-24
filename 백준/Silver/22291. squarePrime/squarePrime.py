p=[1]*(10**5)
for i in range(2,10**5):
    if(p[i]==1):
        for j in range(2*i,10**5,i):
            p[j]=0
def P2(A):
    r=0
    for i,e in enumerate(A):
        if(i>1 and e>0 and p[i] and e**0.5==int(e**0.5)):
            r+=e
    return r