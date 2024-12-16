def t(n,m):
    r=0
    while n>0:
        n,mod=divmod(n,m)
        r+=mod
    return r
for i in range(1000,10000):
    if(t(i,10)==t(i,12)==t(i,16)):
        print(i)