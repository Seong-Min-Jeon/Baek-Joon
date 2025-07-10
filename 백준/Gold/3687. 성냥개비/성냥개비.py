I=input
l=[10**100]*101
l[2],l[3],l[4],l[5],l[6],l[7]=1,7,4,2,0,8
for i in range(101):
    for j in range(2,i):
        if(l[j]==0): l[i]=min(l[i],int(str(6)+str(l[i-j])))
        else: l[i]=min(l[i],int(str(l[j])+str(l[i-j])))
l[6]=6
for _ in range(int(I())):
    n=int(I())
    print(l[n],end=' ')
    if(n%2==0): print('1'*(n//2))
    else: print('7'+'1'*((n-3)//2))