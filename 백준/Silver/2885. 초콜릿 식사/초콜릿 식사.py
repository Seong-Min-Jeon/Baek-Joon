k=int(input())
i=1
while i<k: i*=2
if(k==i): print(i,0); exit()
r=i
c=0
while k:
    r//=2
    if(k>=r): k-=r
    c+=1
print(i,c)