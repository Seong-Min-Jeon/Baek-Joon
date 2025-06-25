n,k=map(int,input().split())
l=list(map(int,input().split()))
for i,e in enumerate(l):
    if((e-i)%k!=0): print('No'); exit()
print('Yes')