import math
I=input
n,m=int(I()),I()
l=list(map(int,I().split()))
p=0
for i in range(len(l)):
    if(i==0): continue
    p=max(p,math.ceil((l[i]-l[i-1])/2))
print(max(l[0],p,n-l[-1]))