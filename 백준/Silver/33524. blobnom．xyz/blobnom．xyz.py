from bisect import bisect_right as B
I,F=input,lambda:map(int,I().split());n,m=F()
a,b,l=sorted([*F()]),[*F()],[3*i*(i-1)+1 for i in range(1,400)]
for e in b:print(B(l,B(a,e)),end=' ')