a,b,n,k=map(int,input().split())
r=(k//n+(k%n!=0))-1
print(r//b+1,r%b+1)