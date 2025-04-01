l=[list(input().strip()) for _ in range(8)]
c=0
for i in range(8):
    for j in range(8):
        if((i+j)%2==0 and l[i][j]=='F'):
            c+=1
print(c)