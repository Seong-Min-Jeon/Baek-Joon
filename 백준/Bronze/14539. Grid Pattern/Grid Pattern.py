a=int(input())
r=[]
for i in range(a):
    l=list(map(int,input().split()))
    r.append(f'Case #{i+1}:')
    b=('+'+'-'*l[2])*l[1]+'+'
    c=('|'+'*'*l[2])*l[1]+'|'
    for j in range(l[0]):
        r.append(b)
        for k in range(l[3]):
            r.append(c)
    r.append(b)
for i in r:
    print(i)