l,m,n=map(float,input().split())
if(l!=n):
    print(0)
    exit(0)
r=round(((l**2*2)**0.5)*(((l+m)**2*2)**0.5),4)
l=str(r).split('.')
l[1]+='0'*(4-len(l[1]))
print(f'{l[0]}.{l[1]}')