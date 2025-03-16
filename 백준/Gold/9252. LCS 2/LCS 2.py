a=list(input().strip())
b=list(input().strip())
l=[[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b[j]): l[i+1][j+1]=l[i][j]+1
        else: l[i+1][j+1]=max(l[i+1][j],l[i][j+1])
c=max(l[-1])
print(c)
t=[]
i,j=len(a),len(b)
while c>0:
    if(l[i-1][j]==l[i][j]): i-=1
    elif(l[i][j-1]==l[i][j]): j-=1
    else: t.append(a[i-1]); i-=1; j-=1; c-=1
print(''.join(reversed(t)))