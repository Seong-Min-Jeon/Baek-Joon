i=input; r=int(i())
for _ in range(r):
    a,b=i().split()
    a=int(a)
    d=''
    for c in b:
        d+=c*a
    print(d)