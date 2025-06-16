n,m,k=map(int,input().split())
o,x=m,n-m
l=n-k
print(min(m,k)+min(x,l))