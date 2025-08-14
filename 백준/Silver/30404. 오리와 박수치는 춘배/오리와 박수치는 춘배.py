n,k,*l=list(map(int,open(0).read().split()))
p,c=l[0]+k,1
for e in l:
 if(p<e):p=e+k;c+=1
print(c)