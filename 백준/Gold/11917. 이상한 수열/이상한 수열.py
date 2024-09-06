i=input
a=int(i())
l=list(map(int,i().split()))
r=int(i())
if(r<=a): print(l[r-1]); exit(0)
b=len(set(l))
for e in sorted(l):
    if(e>=b and e<b+r-a): print(e); exit(0)
l.append(b)
print(l[len(l)-1]+r-a-1)