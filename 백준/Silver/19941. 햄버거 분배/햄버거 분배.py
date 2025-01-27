n,k=map(int,input().split())
l=list(input().strip())
c=0
for i in range(n):
    if(l[i].upper()=='H'): continue
    for j in range(i-k,i+k+1):
        if(j>=0 and j<n and l[j]=='H'): c+=1; l[j]='h'; break
print(c)