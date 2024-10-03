i=input
n,k=map(int,i().split())
l=[]
for _ in range(n):
    l.append(int(i()))
l.reverse()
c=0
for e in l:
    t=k//e
    k-=t*e
    c+=t
print(c)