a,b=input(),input()
l=[[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if(a[j-1]!=b[i-1]): l[i][j]=max(l[i][j-1],l[i-1][j])
        else: l[i][j]=l[i-1][j-1]+1
print(max(map(max,l)))