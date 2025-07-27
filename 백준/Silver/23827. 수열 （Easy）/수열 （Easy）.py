I=input; I()
l=[*map(int,I().split())]
s,r=sum(l),0
for i in range(len(l)): s-=l[i]; r=(r+l[i]*s)%1000000007
print(r)